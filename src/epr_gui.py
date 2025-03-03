import webview
from webview.dom import ManipulationMode
from webview.dom.element import Element
from config_manager import ConfigManager
from data_types.editor_entry import EditorEntry
from epr_popup import EprPopup, EprPopupTypes


class EprGUI:
    __WINDOW_TITLE = "EditorPerRepo"
    __WINDOW_SIZE = (650, 300)
    __WINDOW_HTML_PATH = "static/index.html"


    def __init__(self, config: ConfigManager = None, target_dir: str = None):
        self.window: webview.Window = webview.create_window(self.__WINDOW_TITLE, self.__WINDOW_HTML_PATH,
                                                            width=self.__WINDOW_SIZE[0], height=self.__WINDOW_SIZE[1],
                                                            # min_size=self.__WINDOW_SIZE,
                                                            resizable=False, easy_drag=True, frameless=True)
        self.editor_select: Element = None
        self.editor_select_divider: Element = None

        self.config = config or ConfigManager()
        self.target_dir = target_dir


    def __get_editor_select_children(self, remove_auto_found=False):
        children = self.editor_select.children

        clean_children = list(filter(lambda c: c.id != "auto-found-divider", children))
        if not remove_auto_found:
            return clean_children

        return list(filter(lambda c: not c.attributes.get("auto-found"), clean_children))


    def __add_select_option(self, entry):
        clean_editor_select_children = self.__get_editor_select_children()
        option_index = len(clean_editor_select_children)
        added_option = self.editor_select.append(
            f"<option value='{option_index}'>{entry.path}</option>",
            mode=ManipulationMode.FirstChild)

        if entry.auto_found:
            added_option.attributes["auto-found"] = True

        self.editor_select.value = added_option.value


    def __hide_or_show_auto_found_editors(self):
        for child in self.editor_select.children:
            if child.attributes.get("auto-found"):
                child.show() if self.config.show_found_editors else child.hide()

        visible_options = list(filter(lambda o: o.style["display"] != "none", self.__get_editor_select_children()))
        if not visible_options:
            self.editor_select.value = None
            return

        visible_option_selected = list(filter(lambda option: option.value == self.editor_select.value, visible_options))
        if not visible_option_selected:
            self.editor_select.value = visible_options[0].value


    def __hide_or_show_auto_found_select_divider(self):
        if not self.config.show_found_editors:
            return self.editor_select_divider.hide()

        clean_manual_editor_select_children = self.__get_editor_select_children(remove_auto_found=True)
        if not clean_manual_editor_select_children:
            self.editor_select_divider.hide()
            return

        first_added_not_auto_found_editor = clean_manual_editor_select_children[len(clean_manual_editor_select_children) - 1]
        auto_found_stop_index = clean_manual_editor_select_children.index(first_added_not_auto_found_editor)

        self.editor_select_divider.move(target=self.editor_select.children[auto_found_stop_index], mode=ManipulationMode.After)
        self.editor_select_divider.show()


    def __on_add_editor_click(self, e):
        print("Add editor button clicked")

        file_select = self.window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=False)
        if not file_select:
            print("File select cancelled")
            return

        print(f"Selected file: {file_select}")
        editor = EditorEntry(path=file_select[0])
        self.config.editors.append(editor)
        self.__add_select_option(editor)
        # self.__hide_or_show_auto_found_editors()
        self.__hide_or_show_auto_found_select_divider()
        self.config.save_data()


    def __on_remove_editor_click(self, _):
        selected_option_path = self.__get_selected_option_path()
        print("Removing", selected_option_path)

        selected_editor = list(filter(lambda editor: editor.path == selected_option_path, self.config.editors))
        if selected_editor:
            self.config.editors.remove(selected_editor[0])

        removed_option = list(filter(lambda o: o.value == self.editor_select.value, self.editor_select.children))
        if removed_option:
            removed_option[0].remove()

        self.config.save_data()
        self.__hide_or_show_auto_found_select_divider()


    def __on_show_found_checkbox_change(self, e):
        self.config.show_found_editors = e["target"]["checked"]
        print("Show found editors set to:", self.config.show_found_editors)
        self.__hide_or_show_auto_found_editors()
        self.__hide_or_show_auto_found_select_divider()
        self.config.save_data()


    def __on_submit_click(self, _):
        editor_path = self.__get_selected_option_path()
        if not editor_path:
            print("Submit button pressed with no selected option!")
            return EprPopup().show(EprPopupTypes.SUBMIT_WITH_NO_SELECTED)

        print(f"Setting {self.target_dir} to {editor_path}!")

        self.config.repo_editor_dict[self.target_dir] = editor_path
        self.config.last_used_editor_path = self.__get_selected_option_path()
        self.config.save_data()
        self.window.destroy()


    def __on_loaded(self):
        self.editor_select = self.window.dom.get_element("#editor-select")
        [self.__add_select_option(option) for option in self.config.editors]

        self.editor_select_divider = self.window.dom.get_element("option#auto-found-divider")
        # self.editor_select_divider.text = "-" * 25
        # self.editor_select_divider.test = "─" * 30
        self.editor_select_divider.text = "\U00002500" * 30

        self.show_found_checkbox: Element = self.window.dom.get_element("#show-found-checkbox")
        self.show_found_checkbox.attributes["checked"] = True if self.config.show_found_editors else None
        self.show_found_checkbox.on("change", self.__on_show_found_checkbox_change)
        self.__hide_or_show_auto_found_editors()
        self.__hide_or_show_auto_found_select_divider()

        last_used_editors = list(filter(lambda option: option.text == self.config.last_used_editor_path, self.editor_select.children))
        if last_used_editors:
            self.editor_select.value = last_used_editors[0].value


    def __bind_events(self, _):
        self.window.dom.get_element("#exit-button").on("click", lambda e: self.window.destroy())
        self.window.dom.get_element("#remove-editor-button").on("click", self.__on_remove_editor_click)
        self.window.dom.get_element("#add-editor-button").on("click", self.__on_add_editor_click)
        self.window.dom.get_element("#submit").on("click", self.__on_submit_click)


    def __get_selected_option_path(self):
        options_with_key_value = list(filter(lambda o: o.value == self.editor_select.value, self.editor_select.children))
        if options_with_key_value:
            return options_with_key_value[0].text


    def show(self):
        webview.DRAG_REGION_SELECTOR = "header"
        self.window.events.loaded += self.__on_loaded
        webview.start(self.__bind_events, self.window, ssl=True)
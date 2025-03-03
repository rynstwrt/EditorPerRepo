import webview
from webview.dom import ManipulationMode
from webview.dom.element import Element
from config_manager import ConfigManager
from editor_entry import EditorEntry


class EprGUI:
    __WINDOW_SIZE = (600, 300)


    def __init__(self):
        self.window: webview.Window = None
        self.editor_select: Element = None

        self.config = ConfigManager()
        self.editors = (self.config.editors or []) + (self.config.auto_find_installed_editors() or [])


    def __on_add_editor_click(self, e):
        print("Add editor button clicked")

        file_select = self.window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=False)
        if not file_select:
            print("File select cancelled")
            return

        print(f"Selected file: {file_select}")
        self.add_select_option(EditorEntry(file_select[0]))


    def __on_remove_editor_click(self, e):
        selected_option_path = self.get_select_value()
        print("Removing", selected_option_path)

        selected_editor = list(filter(lambda editor: editor.path == selected_option_path, self.editors))
        if selected_editor:
            self.editors.remove(selected_editor[0])

        removed_option = list(filter(lambda o: o.value == self.editor_select.value, self.editor_select.children))
        if removed_option:
            removed_option[0].remove()


    def __hide_or_show_auto_found_editors(self):
        for child in self.editor_select.children:
            if child.attributes.get("auto_found"):
                child.show() if self.config.show_found_editors else child.hide()

        visible_options = [option for option in self.editor_select.children if option.style["display"] != "none"]
        if not visible_options:
            self.editor_select.value = None
            return

        visible_option_selected = list(filter(lambda option: option.value == self.editor_select.value, visible_options))
        if not visible_option_selected:
            self.editor_select.value = visible_options[0].value


    def __on_show_found_checkbox_change(self, e):
        self.config.show_found_editors = e["target"]["checked"]
        print("Show found editors set to:", self.config.show_found_editors)
        self.__hide_or_show_auto_found_editors()
        self.config.save_data()


    def __on_submit_click(self, e):
        print(self.get_select_value())


    def __bind_events(self, _):
        self.editor_select = self.window.dom.get_element("#editor-select")
        [self.add_select_option(option) for option in self.editors]

        self.show_found_checkbox: Element = self.window.dom.get_element("#show-found-checkbox")
        self.show_found_checkbox.attributes["checked"] = True if self.config.show_found_editors else None
        self.show_found_checkbox.on("change", self.__on_show_found_checkbox_change)
        self.__hide_or_show_auto_found_editors()

        self.window.dom.get_element("#remove-editor-button").on("click", self.__on_remove_editor_click)
        self.window.dom.get_element("#add-editor-button").on("click", self.__on_add_editor_click)
        self.window.dom.get_element("#submit").on("click", self.__on_submit_click)


    def get_select_value(self):
        options_with_key_value = list(filter(lambda o: o.value == self.editor_select.value, self.editor_select.children))
        if options_with_key_value:
            return options_with_key_value[0].text


    def add_select_option(self, entry):
        option_index = len(self.editor_select.children)
        self.editor_select.append(
            f"<option value='{option_index}' auto_found={entry.auto_found}>{entry.path}</option>",
            mode=ManipulationMode.FirstChild)
        self.editor_select.value = option_index


    def create_window(self):
        self.window = webview.create_window("EditorPerRepo","./static/index.html",
                                            width=self.__WINDOW_SIZE[0], height=self.__WINDOW_SIZE[1],
                                            resizable=False)

        webview.start(self.__bind_events, self.window)

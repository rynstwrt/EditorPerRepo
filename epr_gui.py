import webview
from webview.dom import ManipulationMode
from webview.dom.element import Element
from config_manager import ConfigManager


class EprGUI:
    __WINDOW_SIZE = (500, 300)


    def __init__(self):
        self.window: webview.Window = None
        self.editor_select: Element = None

        self.config = ConfigManager()
        self.saved_editor_paths = self.config.get_editor_paths() or []
        self.found_editor_paths = self.config.auto_find_installed_editors() if self.config.should_show_found_editors() else []


    def __on_add_editor_click(self, e):
        print("Add editor button clicked")

        file_select = self.window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=False)
        if not file_select:
            print("File select cancelled")
            return

        print(f"Selected file: {file_select}")
        self.add_select_option(file_select[0])


    def __hide_or_show_auto_found_editors(self):
        for child in self.editor_select.children:
            if child.attributes.get("auto_found"):
                child.show() if self.config.should_show_found_editors() else child.hide()

        visible_options = [option for option in self.editor_select.children if option.style["display"] != "none"]

        selected_visible_options = [option for option in visible_options if self.editor_select.value == option.value]
        if visible_options and not selected_visible_options:
            self.editor_select.value = visible_options[0].value


    def __on_show_found_checkbox_change(self, e):
        is_checked = e["target"]["checked"]
        self.config.set_show_found_editors(is_checked)
        print("Show found editors set to:", self.config.should_show_found_editors())
        self.__hide_or_show_auto_found_editors()


    def __on_submit_click(self, e):
        print(self.get_select_value())


    def __bind_events(self, _):
        self.editor_select = self.window.dom.get_element("#editor-select")
        [self.add_select_option(editor_path) for editor_path in self.saved_editor_paths]
        [self.add_select_option(found_editor_path, True) for found_editor_path in self.found_editor_paths]

        self.show_found_checkbox: Element = self.window.dom.get_element("#show-found-checkbox")
        self.show_found_checkbox.attributes["checked"] = self.config.should_show_found_editors()
        self.show_found_checkbox.on("change", self.__on_show_found_checkbox_change)
        self.__hide_or_show_auto_found_editors()

        self.window.dom.get_element("#add-editor-button").on("click", self.__on_add_editor_click)
        self.window.dom.get_element("#submit").on("click", self.__on_submit_click)


    def get_select_value(self):
        select_child_index = len(self.editor_select.children) - int(self.editor_select.value) - 1
        return self.editor_select.children[select_child_index].text


    def add_select_option(self, value, auto_found=False):
        option_index = len(self.editor_select.children)
        self.editor_select.append(
            f"<option value='{option_index}'{" auto_found=True" if auto_found else ""}>{value}</option>",
            mode=ManipulationMode.FirstChild)
        self.editor_select.value = option_index


    def create_window(self):
        self.window = webview.create_window("EditorPerRepo","./static/index.html",
                                            width=self.__WINDOW_SIZE[0], height=self.__WINDOW_SIZE[1],
                                            resizable=False)

        webview.start(self.__bind_events, self.window)

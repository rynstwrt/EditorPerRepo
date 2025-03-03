import webview
from webview.dom import ManipulationMode
from webview.dom.element import Element


class EprGUI:
    __WINDOW_SIZE = (500, 300)


    def __init__(self, saved_editor_paths):
        self.window = None
        self.select: Element = None
        self.saved_editor_paths = saved_editor_paths or []


    def __on_add_editor_click(self, e):
        print("Add editor button clicked")

        file_select = self.window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=False)
        if not file_select:
            print("File select cancelled")
            return

        print(f"Selected file: {file_select}")
        self.add_select_option(file_select[0])


    def __on_submit_click(self, e):
        print(self.get_select_value())


    def __bind_events(self, _):
        self.select = self.window.dom.get_element("#editor-select")
        [self.add_select_option(editor_path) for editor_path in self.saved_editor_paths]

        self.window.dom.get_element("#submit").on("click", self.__on_submit_click)
        self.window.dom.get_element("#add-editor-button").on("click", self.__on_add_editor_click)


    def get_select_value(self):
        select_child_index = len(self.select.children) - int(self.select.value) - 1
        return self.select.children[select_child_index].text


    def add_select_option(self, value):
        option_index = len(self.select.children)
        self.select.append(f"<option value='{option_index}'>{value}</option>",
                           mode=ManipulationMode.FirstChild)
        self.select.value = option_index


    def create_window(self):
        self.window: webview.Window = webview.create_window("EditorPerRepo",
                                                            "./static/index.html",
                                                            width=self.__WINDOW_SIZE[0],
                                                            height=self.__WINDOW_SIZE[1],
                                                            resizable=False)

        webview.start(self.__bind_events, self.window)

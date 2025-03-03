from enum import Enum, auto
import webview


class EprPopupTypes(Enum):
    INVALID_DIR = auto()
    INVALID_EDITOR = auto()


class EprPopup:
    __POPUP_TITLE = "EPR Popup"
    __POPUP_HTML_PATH = "./static/popup.html"
    __POPUP_SIZE = (350, 250)
    __POPUP_MESSAGES = {
        EprPopupTypes.INVALID_DIR: "dir",
        EprPopupTypes.INVALID_EDITOR: "editor"
    }


    def __init__(self):
        self.popup_type = None
        self.window: webview.Window = webview.create_window(self.__POPUP_TITLE, self.__POPUP_HTML_PATH,
                                                            width=self.__POPUP_SIZE[0], height=self.__POPUP_SIZE[1],
                                                            resizable=False, frameless=True, easy_drag=True)


    def __create_content(self):
        self.window.dom.get_element("#popup-text").text = self.__POPUP_MESSAGES[self.popup_type]


    def __bind_events(self, _):
        self.window.dom.get_element("#exit-button").on("click", lambda e: self.window.destroy())


    def show(self, popup_type: EprPopupTypes):
        self.popup_type = popup_type
        webview.DRAG_REGION_SELECTOR = "header"
        self.window.events.loaded += self.__create_content
        webview.start(self.__bind_events, self.window, ssl=True)
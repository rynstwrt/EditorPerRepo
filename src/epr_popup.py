import webview
from enum import Enum, auto


class EprPopupTypes(Enum):
    TARGET_DIR_NOT_SPECIFIED = auto()
    TARGET_DIR_NOT_EXIST = auto()
    EDITOR_NOT_EXIST = auto()
    SUBMIT_WITH_NO_SELECTED = auto()


class EprPopup:
    __POPUP_TITLE = "EditorPerRepo Error"
    __POPUP_HTML_PATH = "static/popup.html"
    __POPUP_SIZE = (550, 300)
    __POPUP_TEXTS = {
        EprPopupTypes.TARGET_DIR_NOT_SPECIFIED: "The target directory to open was not specified!",
        EprPopupTypes.TARGET_DIR_NOT_EXIST: "The target directory does not exist!",
        EprPopupTypes.EDITOR_NOT_EXIST: "The chosen editor does not exist!",
        EprPopupTypes.SUBMIT_WITH_NO_SELECTED: "No editor was selected!"
    }


    def __init__(self):
        self.popup_type = None
        self.given_path = None
        self.window: webview.Window = webview.create_window(self.__POPUP_TITLE, self.__POPUP_HTML_PATH,
                                                            width=self.__POPUP_SIZE[0], height=self.__POPUP_SIZE[1],
                                                            resizable=False, frameless=True, easy_drag=True)


    def __create_content(self):
        self.window.dom.get_element("#exit-button").on("click", lambda e: self.window.destroy())

        self.window.dom.get_element("#popup-text").text = self.__POPUP_TEXTS[self.popup_type]

        popup_details = self.window.dom.get_element("#popup-details")
        popup_details_display_style = popup_details.style["display"]
        popup_details.style["display"] = popup_details_display_style if self.given_path else "none"
        popup_details.text = f'({(self.given_path or "").replace("\\", "\\\\")})'


    def show(self, popup_type: EprPopupTypes, given_path: str = None):
        self.popup_type = popup_type
        self.given_path = given_path

        webview.DRAG_REGION_SELECTOR = "header"
        self.window.events.loaded += self.__create_content

        # self.window.show() if webview.active_window() else webview.start(None, self.window, ssl=True)
        if webview.active_window():
            self.window.show()
        else:
            webview.start(None, self.window, ssl=True)
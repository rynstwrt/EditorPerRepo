import FreeSimpleGUI as sg
from util.global_constants import *


WINDOW_TITLE = "EditorPerRepo"
CONFIG_WINDOW_TITLE = "EditorPerRepo Config"
WARNING_POPUP_TITLE = "WARNING"

THEME = "Dark Grey 15"
FONT = ("Helvetica Neue Light", 12)

DEFAULT_WINDOW_SIZE = (500, 250)
DEFAULT_CONFIG_WINDOW_SIZE = (500, 500)
SMALL_BUTTON_SIZE = (8, 1)
VERY_SMALL_BUTTON_SIZE = (4, 1)
MEDIUM_BUTTON_SIZE = (11, 1)
SCROLL_BAR_WIDTH = 8


class EprGui:
    def __init__(self, editors):
        sg.theme(THEME)
        self._editors = editors
        self._list_menu_items = [editor["name"] for editor in editors]


    def create_window(self):
        layout = [
            [
                sg.Text("Please select an editor to open this directory:",
                        justification="c",
                        pad=((0, 0), (0, 7)))
            ],
            [
                sg.Listbox(key=EDITOR_LIST_KEY,
                           values=self._list_menu_items,
                           expand_x=True,
                           expand_y=True,
                           font=(FONT[0], FONT[1] - 1),
                           select_mode=sg.SELECT_MODE_SINGLE,
                           pad=((5, 5), (0, 0)))
            ],
            [
                # sg.Text("Save selection:"),
                sg.Checkbox(key=SAVE_SELECTION_CHECKBOX_KEY,
                            text="Save selection",
                            default=True,
                            pad=((0, 0), (0, 7)),
                            font=(FONT[0], FONT[1] - 1)),
                sg.Push()
            ],
            [
                sg.Button("Cancel",
                          size=SMALL_BUTTON_SIZE,
                          font=FONT),
                sg.Button(key=OPEN_CONFIG_KEY,
                          button_text="Config",
                          size=SMALL_BUTTON_SIZE,
                          font=FONT),
                sg.Button(key=SUBMIT_KEY,
                          button_text="Submit",
                          expand_x=True,
                          font=FONT)
            ],
        ]

        return sg.Window(WINDOW_TITLE,
                         layout=layout,
                         size=DEFAULT_WINDOW_SIZE,
                         element_justification="c",
                         font=FONT,
                         margins=(7, 7),
                         auto_size_text=False,
                         auto_size_buttons=False,
                         sbar_width=SCROLL_BAR_WIDTH,
                         sbar_arrow_width=SCROLL_BAR_WIDTH)


# TODO:
class EprConfigGUI:
    def __init__(self, editors):
        sg.theme(THEME)
        self._editors = editors
        self._editor_list_menu_items = self._list_menu_items = [editor["name"] for editor in editors]
        self._list_menu_association_items = ["(Coming Soon)"]


    def create_window(self):
        layout = [
            [
                sg.Text("Add or Remove Editors:",
                        expand_x=True,
                        pad=((5, 0), (0, 7)))
            ],
            [
                sg.Listbox(key=CONFIG_EDITOR_LIST_KEY,
                           values=self._editor_list_menu_items,
                           expand_x=True,
                           expand_y=True,
                           font=(FONT[0], FONT[1] - 1),
                           select_mode=sg.SELECT_MODE_SINGLE,
                           pad=((5, 5), (0, 4)))
            ],
            [
                sg.Button(key=CONFIG_EDITOR_REMOVE_KEY,
                          button_text="-",
                          size=VERY_SMALL_BUTTON_SIZE,
                          font=FONT),
                sg.Button(key=CONFIG_EDITOR_ADD_KEY,
                          button_text="+",
                          size=VERY_SMALL_BUTTON_SIZE,
                          font=FONT),
                sg.Button(key=CONFIG_EDITOR_RENAME_KEY,
                          button_text="Rename",
                          size=MEDIUM_BUTTON_SIZE,
                          font=FONT),
                sg.Button(key=CONFIG_EDITOR_DETECT_KEY,
                          button_text="Detect",
                          size=MEDIUM_BUTTON_SIZE,
                          font=FONT),
                sg.Button(key=CONFIG_SAVE_KEY,
                          button_text="Save",
                          expand_x=True,
                          font=FONT)
            ],

            [
                sg.HSeparator(color="black", pad=((5, 5), (15, 15)))
            ],

            [
                sg.Text("Remove Directory Associations:",
                        expand_x=True,
                        pad=((5, 0), (0, 7)))
            ],
            [
                sg.Listbox(key=CONFIG_EDITOR_REMOVE_ASSOCIATIONS_KEY,
                           values=self._list_menu_association_items,
                           expand_x=True,
                           expand_y=True,
                           font=(FONT[0], FONT[1] - 1),
                           select_mode=sg.SELECT_MODE_SINGLE,
                           pad=((5, 5), (0, 4)))
            ],
            [
                sg.Button(key="",
                          button_text="Remove",
                          size=MEDIUM_BUTTON_SIZE,
                          font=FONT),
                sg.Button(key=CONFIG_SAVE_KEY,
                          button_text="Save",
                          expand_x=True,
                          font=FONT)
            ]
        ]

        return sg.Window(CONFIG_WINDOW_TITLE,
                         layout=layout,
                         size=DEFAULT_CONFIG_WINDOW_SIZE,
                         font=FONT,
                         margins=(7, 7),
                         auto_size_text=False,
                         auto_size_buttons=False,
                         sbar_width=SCROLL_BAR_WIDTH,
                         sbar_arrow_width=SCROLL_BAR_WIDTH)


def make_warning_popup(reason):
    sg.popup(title=WARNING_POPUP_TITLE,
             any_key_closes=True,
             custom_text=reason.upper(),
             button_type=sg.POPUP_BUTTONS_ERROR)
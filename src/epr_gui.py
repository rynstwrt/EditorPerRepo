import FreeSimpleGUI as sg
from src.util import epr_util
from util.global_constants import *
from pathlib import Path


WINDOW_TITLE = "EditorPerRepo"
CONFIG_WINDOW_TITLE = "EditorPerRepo Config"
WARNING_POPUP_TITLE = "WARNING"

FONT = ("Helvetica Neue Light", 12)

EXIT_ICON_PATH = "./assets/icons/x2.png"

DEFAULT_WINDOW_SIZE = (500, 250)
DEFAULT_CONFIG_WINDOW_SIZE = (600, 500)
SMALL_BUTTON_SIZE = (8, 1)
VERY_SMALL_BUTTON_SIZE = (4, 1)
MEDIUM_BUTTON_SIZE = (11, 1)
SCROLL_BAR_WIDTH = 8

TITLEBAR_COLOR = "#272a30"

WINDOW_PADDING = ((11, 11), (15, 9))
TAB_BUTTON_PADDING = (2, 3)
MAIN_COLUMN_PADDING = ((10, 10), (10, 8))
LISTBOX_PADDING = ((5, 5), (10, 5))


TITLEBAR = sg.Column(layout=[
    [
        sg.Image(key=EXIT_ICON_KEY,
                 filename=epr_util.get_parsed_abs_path(EXIT_ICON_PATH, Path(__file__).parent),
                 subsample=2,
                 enable_events=True,
                 background_color=TITLEBAR_COLOR,
                 pad=((0, 7), (3, 2)))
    ]
],
    background_color=TITLEBAR_COLOR,
    expand_x=True,
    element_justification="r",
    grab=True)


sg.set_options(element_padding=(0, 0),
               auto_size_text=False,
               auto_size_buttons=False,
               font=FONT,
               keep_on_top=True)


class EprGui:
    def __init__(self, editors):
        self._editors = editors
        self._list_menu_items = [editor["name"] for editor in editors]


    def create_window(self):
        main_column_layout = [
            [
                sg.Text("Please select an editor to open this directory:",
                        justification="c",
                        expand_x=True,
                        pad=((0, 0), (0, 5)))
            ],
            [
                sg.Listbox(key=EDITOR_LIST_KEY,
                           values=self._list_menu_items,
                           expand_x=True,
                           expand_y=True,
                           font=(FONT[0], FONT[1] - 1),
                           select_mode=sg.SELECT_MODE_SINGLE)
            ],
            [
                sg.Checkbox(key=SAVE_SELECTION_CHECKBOX_KEY,
                            text="Save selection",
                            default=True,
                            pad=((0, 0), (2, 7)),
                            font=(FONT[0], FONT[1] - 1)),
                sg.Push()
            ],
            [
                sg.Button("Cancel",
                          size=SMALL_BUTTON_SIZE,
                          font=FONT,
                          pad=TAB_BUTTON_PADDING),
                sg.Button(key=OPEN_CONFIG_KEY,
                          button_text="Config",
                          size=SMALL_BUTTON_SIZE,
                          font=FONT,
                          pad=TAB_BUTTON_PADDING),
                sg.Button(key=SUBMIT_KEY,
                          button_text="Submit",
                          expand_x=True,
                          font=FONT,
                          pad=TAB_BUTTON_PADDING),
            ]
        ]

        layout = [
            [TITLEBAR],
            [
                sg.Column(layout=main_column_layout,
                          pad=MAIN_COLUMN_PADDING,
                          expand_x=True,
                          expand_y=True)
            ]
        ]

        return sg.Window(WINDOW_TITLE,
                         layout=layout,
                         size=DEFAULT_WINDOW_SIZE,
                         sbar_width=SCROLL_BAR_WIDTH,
                         sbar_arrow_width=SCROLL_BAR_WIDTH,
                         no_titlebar=True,
                         margins=(0, 0),
                         element_justification="c",
                         finalize=True)


class EprConfigGUI:
    def __init__(self, editors):
        self._editors = editors
        self._editor_list_menu_items = self._list_menu_items = [editor["name"] for editor in editors]
        self._list_menu_association_items = ["(Coming Soon)"]

        sg.set_options(element_padding=(0, 0),
                       auto_size_text=False,
                       auto_size_buttons=False,
                       font=FONT,
                       keep_on_top=True)

        self.add_remove_editor_tab_layout = [
            [
                sg.Listbox(key=CONFIG_EDITOR_LIST_KEY,
                           values=self._editor_list_menu_items,
                           expand_x=True,
                           expand_y=True,
                           font=(FONT[0], FONT[1] - 1),
                           select_mode=sg.SELECT_MODE_SINGLE,
                           pad=LISTBOX_PADDING)
            ],
            [
                sg.Button(key=CONFIG_EDITOR_REMOVE_KEY,
                          button_text="-",
                          size=VERY_SMALL_BUTTON_SIZE,
                          font=FONT, pad=(4, 0)),
                sg.Button(key=CONFIG_EDITOR_ADD_KEY,
                          button_text="+",
                          size=VERY_SMALL_BUTTON_SIZE,
                          font=FONT, pad=TAB_BUTTON_PADDING),
                sg.Button(key=CONFIG_EDITOR_RENAME_KEY,
                          button_text="Rename",
                          size=MEDIUM_BUTTON_SIZE,
                          font=FONT, pad=TAB_BUTTON_PADDING),
                sg.Button(key=CONFIG_EDITOR_DETECT_KEY,
                          button_text="Detect",
                          size=MEDIUM_BUTTON_SIZE,
                          font=FONT, pad=TAB_BUTTON_PADDING),
                sg.Button(key=CONFIG_SAVE_KEY,
                          button_text="Save",
                          expand_x=True,
                          font=FONT, pad=TAB_BUTTON_PADDING),
            ],
        ]

        self.remove_associations_tab_layout = [
            [
                sg.Listbox(key=CONFIG_EDITOR_REMOVE_ASSOCIATIONS_KEY,
                           values=self._list_menu_association_items,
                           expand_x=True,
                           expand_y=True,
                           font=(FONT[0], FONT[1] - 1),
                           select_mode=sg.SELECT_MODE_SINGLE,
                           pad=LISTBOX_PADDING)
            ],
            [
                sg.Button(key="",
                          button_text="Remove",
                          size=MEDIUM_BUTTON_SIZE,
                          pad=(4, TAB_BUTTON_PADDING[1]),
                          font=FONT),
                sg.Button(key=CONFIG_SAVE_KEY,
                          button_text="Save",
                          expand_x=True,
                          pad=TAB_BUTTON_PADDING,
                          font=FONT)
            ]
        ]


    def create_window(self):
        selected_background_color = sg.theme_button_color_background()
        accent_color = sg.theme_button_color_text()
        default_text_color = sg.theme_text_color()

        tab_layout = [
            [
                sg.Tab(title="Change",
                       layout=[*self.add_remove_editor_tab_layout],
                       expand_x=True,
                       expand_y=True,
                       background_color=selected_background_color,
                       element_justification="c")
            ],
            [
                sg.Tab(title="Editor Associations",
                       layout=[*self.remove_associations_tab_layout],
                       expand_x=True,
                       expand_y=True,
                       background_color=selected_background_color)
            ]
        ]

        tab_group = [
            sg.TabGroup(layout=tab_layout,
                        expand_x=True,
                        expand_y=True,
                        border_width=1,
                        tab_border_width=1,
                        title_color=default_text_color,
                        selected_title_color=accent_color,
                        selected_background_color=selected_background_color),
        ]

        layout = [
            [TITLEBAR],
            [
                sg.Column(layout=[tab_group],
                          expand_x=True,
                          expand_y=True,
                          element_justification="c",
                          pad=MAIN_COLUMN_PADDING)
            ]
        ]

        return sg.Window(CONFIG_WINDOW_TITLE,
                         layout=layout,
                         size=DEFAULT_CONFIG_WINDOW_SIZE,
                         sbar_width=SCROLL_BAR_WIDTH,
                         sbar_arrow_width=SCROLL_BAR_WIDTH,
                         no_titlebar=True,
                         titlebar_background_color=TITLEBAR_COLOR,
                         margins=(0, 0),
                         element_justification="c",
                         finalize=True)


def make_warning_popup(reason):
    sg.popup(title=WARNING_POPUP_TITLE,
             any_key_closes=True,
             custom_text=reason.upper(),
             button_type=sg.POPUP_BUTTONS_ERROR)

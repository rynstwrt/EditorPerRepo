from util.constants import *
import FreeSimpleGUI as sg


class EprGui:
    def __init__(self, list_menu_items):
        self._list_menu_items = list_menu_items


    def create_window(self):
        layout = [
            [sg.Text("Please select an editor to open this directory:")],
            [
                sg.Listbox(key=EDITOR_LIST_KEY,
                           values=self._list_menu_items,
                           expand_x=True,
                           expand_y=True,
                           font=(FONT[0], FONT[1] - 1),
                           select_mode=sg.SELECT_MODE_SINGLE,
                           pad=((5, 5), (7, 7)))
            ],
            [
                sg.Button("Cancel",
                          size=SMALL_BUTTON_SIZE),
                sg.Button(key=OPEN_CONFIG_KEY,
                          button_text="Config",
                          size=SMALL_BUTTON_SIZE),
                sg.Button(key=SUBMIT_KEY,
                          button_text="Submit",
                          expand_x=True)
            ],
        ]

        return sg.Window(WINDOW_TITLE,
                         layout=layout,
                         size=DEFAULT_WINDOW_SIZE,
                         element_justification="c",
                         font=FONT,
                         margins=(7, 7))


    @staticmethod
    def make_warning_popup(reason):
        sg.popup(title=WARNING_POPUP_TITLE,
                 any_key_closes=True,
                 custom_text=reason.upper(),
                 button_type=sg.POPUP_BUTTONS_ERROR)

import FreeSimpleGUI as sg
from constants import *


def make_warning_popup(reason):
    sg.popup(title=WARNING_POPUP_TITLE,
             any_key_closes=True,
             custom_text=reason.upper(),
             button_type=sg.POPUP_BUTTONS_ERROR)


def on_submit_button_press(vals):
    print("ayy", vals)

    selected_val = vals["editor-list"]
    if not selected_val:
        return make_warning_popup("No editor was selected")

    return selected_val[0]


def on_open_config_press():
    print("open config")


if __name__ == "__main__":
    window = sg.Window(WINDOW_TITLE,
                       layout=LAYOUT,
                       size=DEFAULT_WINDOW_SIZE,
                       element_justification="c",
                       font=FONT,
                       element_padding=0)

    selected_editor = None
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break

        if event == OPEN_CONFIG_KEY:
            on_open_config_press()

        if event == SUBMIT_KEY:
            selected_editor = on_submit_button_press(values)
            if selected_editor:
                break

    if selected_editor:
        print("VALID SELECTED:", selected_editor)

    window.close()

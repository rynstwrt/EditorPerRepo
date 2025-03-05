import FreeSimpleGUI as sg


WINDOW_TITLE = "EditorPerRepo"
DEFAULT_WINDOW_SIZE = (500, 300)
WARNING_POPUP_TITLE = "WARNING"

FONT = ("Helvetica Neue Light", 14)

EDITOR_LIST_KEY = "editor-list"
SUBMIT_KEY = "submit-button"

THEME = "Dark Grey 15"
sg.theme(THEME)


LAYOUT = [
    [sg.VPush()],
    [sg.Text("Please select an editor to open this repository with:")],
    [
        sg.Listbox(key=EDITOR_LIST_KEY,
                   values=[1, 2, 3, 4],
                   expand_x=True,
                   expand_y=False,
                   size=(None, 5),
                   font=(FONT[0], FONT[1] - 2),
                   select_mode=sg.SELECT_MODE_SINGLE)
    ],
    [
        sg.Button("Cancel"),
        sg.Button(key=SUBMIT_KEY, button_text="Submit")
    ],
    [sg.VPush()]
]


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
                       font=FONT)

    selected_editor = None
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break

        if event == SUBMIT_KEY:
            selected_editor = on_submit_button_press(values)
            if selected_editor:
                break

    if selected_editor:
        print("VALID SELECTED:", selected_editor)


    window.close()

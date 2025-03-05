import FreeSimpleGUI as sg

WINDOW_TITLE = "EditorPerRepo"
DEFAULT_WINDOW_SIZE = (500, 300)
WARNING_POPUP_TITLE = "WARNING"

SMALL_BUTTON_SIZE = (6, 1)
BUTTON_PAD = 2
FONT = ("Helvetica Neue Light", 14)

EDITOR_LIST_KEY = "editor-list"
OPEN_CONFIG_KEY = "config-button"
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
        sg.Button("Cancel", size=SMALL_BUTTON_SIZE, pad=((0, BUTTON_PAD), (0, 0))),
        sg.Button(key=OPEN_CONFIG_KEY, button_text="Config", size=SMALL_BUTTON_SIZE, pad=((BUTTON_PAD, 0), (0, 0)))
    ],
    [sg.Button(key=SUBMIT_KEY,
               button_text="Submit",
               size=(SMALL_BUTTON_SIZE[0] * 2 + BUTTON_PAD // 2, None),
               pad=((0, 0), (BUTTON_PAD * 2, 0)))],
    [sg.VPush()]
]
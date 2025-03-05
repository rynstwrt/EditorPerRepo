import tomllib as toml
from pathlib import Path
from constants import *


def make_warning_popup(reason):
    sg.popup(title=WARNING_POPUP_TITLE,
             any_key_closes=True,
             custom_text=reason.upper(),
             button_type=sg.POPUP_BUTTONS_ERROR)


def on_submit_button_press():
    print("ayy", selected_editor)


def on_open_config_press():
    print("open config")


def load_config():
    config_path = Path(__file__).parent / Path(CONFIG_FILE)
    if not config_path.exists():
        return False, f"Error finding config! Path given: {config_path}"

    try:
        with open(config_path, "rb") as file:
            config_data = toml.load(file)
            file.close()
    except Exception as err:
        print(err)
        return False, "Error while reading config!"

    editors = config_data["editor"]
    if not editors:
        return False, "No editors were found in the config!"

    return True, editors


window = None
def create_window(list_menu_items):
    layout = [
        [sg.Text("Please select an editor to open this directory:")],
        [
            sg.Listbox(key=EDITOR_LIST_KEY,
                       values=list_menu_items,
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

    global window
    window = sg.Window(WINDOW_TITLE,
                       layout=layout,
                       size=DEFAULT_WINDOW_SIZE,
                       element_justification="c",
                       font=FONT,
                       margins=(7, 7))


if __name__ == "__main__":
    list_menu_items = []
    success, config_data = load_config()
    if not success:
        make_warning_popup(str(CONFIG_FILE))
    else:
        editor_paths = [editor["path"] for editor in config_data]
        create_window(editor_paths)

        selected_editor = None
        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "Cancel":
                break

            if event in [SUBMIT_KEY, OPEN_CONFIG_KEY]:
                selected_editor = window[EDITOR_LIST_KEY].get()
                if not not selected_editor:
                    selected_editor = selected_editor[0]

                    if event == SUBMIT_KEY:
                        on_submit_button_press()
                    elif event == OPEN_CONFIG_KEY:
                        on_open_config_press()
                else:
                    make_warning_popup("No editor is selected!")

        if selected_editor:
            print("VALID SELECTED:", selected_editor)

    window.close()

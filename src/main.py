from constants import *
from config_manager import ConfigManager


def make_warning_popup(reason):
    sg.popup(title=WARNING_POPUP_TITLE,
             any_key_closes=True,
             custom_text=reason.upper(),
             button_type=sg.POPUP_BUTTONS_ERROR)


def on_submit_button_press(selected_editor):
    print("ayy", selected_editor)


def on_open_config_press(selected_editor):
    print("open config in", selected_editor)


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

    window = sg.Window(WINDOW_TITLE,
                       layout=layout,
                       size=DEFAULT_WINDOW_SIZE,
                       element_justification="c",
                       font=FONT,
                       margins=(7, 7))

    return window


def main():
    config_manager = ConfigManager(CONFIG_FILE)
    success, config_data = config_manager.load_config()

    if not success:
        return make_warning_popup(str(config_data))

    editor_paths = [editor["path"] for editor in config_data]
    window = create_window(editor_paths)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break

        if event in [SUBMIT_KEY, OPEN_CONFIG_KEY]:
            selected_editor = window[EDITOR_LIST_KEY].get()
            if not selected_editor:
                make_warning_popup("No editor is selected!")
                continue

            if event == SUBMIT_KEY:
                on_submit_button_press(selected_editor[0])
            elif event == OPEN_CONFIG_KEY:
                on_open_config_press(selected_editor[0])

    window.close()


if __name__ == "__main__":
    main()

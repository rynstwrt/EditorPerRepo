from constants import *
from config_manager import ConfigManager
from src.erp_gui import ErpGui


def on_submit_button_press(selected_editor):
    print("ayy", selected_editor)


def on_open_config_press(selected_editor):
    print("open config in", selected_editor)


def main():
    config_manager = ConfigManager(CONFIG_FILE)
    success, config_data = config_manager.load_config()

    if not success:
        return ErpGui.make_warning_popup(str(config_data))

    editor_paths = [editor["path"] for editor in config_data]
    window = ErpGui(editor_paths).create_window()

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break

        if event in [SUBMIT_KEY, OPEN_CONFIG_KEY]:
            selected_editor = window[EDITOR_LIST_KEY].get()
            if not selected_editor:
                ErpGui.make_warning_popup("No editor is selected!")
                continue

            if event == SUBMIT_KEY:
                on_submit_button_press(selected_editor[0])
            elif event == OPEN_CONFIG_KEY:
                on_open_config_press(selected_editor[0])

    window.close()


if __name__ == "__main__":
    main()

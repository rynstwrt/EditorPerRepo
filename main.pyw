import webview
from webview.dom import ManipulationMode
from webview.dom.element import Element


WINDOW_SIZE = (500, 300)


select: Element = None


def get_saved_editor_paths():
    return [f"Path {i + 1}" for i in range(10)]


def get_select_value():
    global select
    select_child_index = select.value
    return select.children[len(select.children) - int(select_child_index) - 1].text


def set_select_value(option_index):
    global select
    select.value = option_index


def add_select_option(value):
    global select
    option_index = len(select.children)
    select.append(f"<option value='{option_index}'>{value}</option>",
                  mode=ManipulationMode.FirstChild)

    set_select_value(option_index)


def on_add_editor_click(e):
    print("adding")

    file_select = window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=False)
    if not file_select:
        print("File select cancelled")
        return

    print(f"Selected file: {file_select}")
    add_select_option(file_select[0])


def on_submit_click(e):
    print(get_select_value())


def bind_events(_):
    global select
    select = window.dom.get_element("#editor-select")
    [add_select_option(editor_path) for editor_path in get_saved_editor_paths()]

    window.dom.get_element("#submit").on("click", on_submit_click)
    window.dom.get_element("#add-editor-button").on("click", on_add_editor_click)


if __name__ == "__main__":
    window: webview.Window = webview.create_window("EditorPerRepo",
                                                   "./static/index.html",
                                                   width=WINDOW_SIZE[0], height=WINDOW_SIZE[1],
                                                   resizable=False)

    webview.start(bind_events, window)

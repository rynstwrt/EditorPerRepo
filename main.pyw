import webview
from webview.dom.element import Element


WINDOW_SIZE = (500, 300)


select: Element = None


def get_saved_editor_paths():
    return ["asdfasdf", "meme"]


def get_select_value():
    return window.dom.get_element("#editor-select").value


def set_select_value(value):
    global select
    select.value = str(value)


def add_select_option(value):
    global select
    select.append(f"<option value='{value}'>{value}</option>")
    option_elements = window.dom.get_elements("option")
    set_select_value(option_elements[len(option_elements)-1].value)


def on_add_editor_click(e):
    print("adding")

    file_select = window.create_file_dialog()
    if not file_select:
        print("File select cancelled")
        return

    print(f"Selected file: {file_select}")
    add_select_option(file_select[0])
    set_select_value(file_select[0])


def on_submit_click(e):
    print(get_select_value())
    # window.destroy()
    # print(e["target"]["id"])


def bind_events(_):
    global select
    select = window.dom.get_element("#editor-select")

    editor_paths = get_saved_editor_paths()
    [add_select_option(editor_path) for editor_path in editor_paths]

    window.dom.get_element("#submit-button").on("click", on_submit_click)
    window.dom.get_element("#add-editor-button").on("click", on_add_editor_click)


if __name__ == "__main__":
    window: webview.Window = webview.create_window("EditorPerRepo",
                                                   "./static/index.html",
                                                   width=WINDOW_SIZE[0], height=WINDOW_SIZE[1],
                                                   resizable=False)

    webview.start(bind_events, window)

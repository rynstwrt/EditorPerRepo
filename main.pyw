import webview


WINDOW_SIZE = (500, 300)
# WINDOW_POSITION = (500, 500)


select_value = None


def on_select_change(e):
    print(e["target"]["value"])


def on_submit_click(e):
    print(e)
    print(e["target"]["id"])


def bind_events(_):
    global select_value

    window.dom.get_element("#submit-button").on("click", on_submit_click)

    select = window.dom.get_element("#editor-select")
    select.on("change", on_select_change)
    select_value = select.value
    print(select_value)


if __name__ == "__main__":
    window: webview.Window = webview.create_window("EditorPerRepo",
                                                   "./static/test.html",
                                                   width=WINDOW_SIZE[0], height=WINDOW_SIZE[1],
                                                   resizable=False)

    webview.start(bind_events, window)

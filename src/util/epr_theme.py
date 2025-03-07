import FreeSimpleGUI as sg


THEME_NAME = "ryn"
# THEME_DICT = {
#     "BACKGROUND": "#ff6600",
#     "TEXT": "#ff6600",
#     "tab_background_color": "orange",
#     "INPUT": "blue",
#     "TEXT_INPUT": "purple",
#     "SCROLL": "white",
#     "BUTTON": ("#FF6600", "#FF00FF"),
#     "PROGRESS": ("#FF6600", "#FF00FF"),
#     "BORDER": 0,
#     "SLIDER_DEPTH": 0,
#     "PROGRESS_DEPTH": 0
# }






BG_COLOR = "#121212"
TEXT_COLOR = "#fcfcfc"

INPUT_COLOR = "#1e1e1e"
INPUT_TEXT_COLOR = "#dedede"

BUTTON_BG_COLOR = "#2e2e2e"
BUTTON_FG_COLOR = "#69b1d0"

SCROLL_BAR_COLOR = "#0d0d0d"

PROGRESS_BAR_BG_COLOR = "#2e2e2e"
PROGRESS_BAR_FG_COLOR = "#69b1d0"

BORDER_THICKNESS = 1
SLIDER_DEPTH = 1
PROGRESS_DEPTH = 1


THEME_DICT = {
    "BACKGROUND": BG_COLOR,
    "TEXT": TEXT_COLOR,
    "INPUT": INPUT_COLOR,
    "TEXT_INPUT": INPUT_TEXT_COLOR,
    "SCROLL": SCROLL_BAR_COLOR,
    "BUTTON": (BUTTON_FG_COLOR, BUTTON_BG_COLOR),
    "PROGRESS": (PROGRESS_BAR_FG_COLOR, PROGRESS_BAR_BG_COLOR),
    "BORDER": BORDER_THICKNESS,
    "SLIDER_DEPTH": SLIDER_DEPTH,
    "PROGRESS_DEPTH": PROGRESS_DEPTH
}


def create_theme():
    sg.theme_add_new(THEME_NAME, THEME_DICT)
    # sg.theme("Dark Grey 15")
    sg.theme(THEME_NAME)
    # sg.popup_get_text("hewwo")
import FreeSimpleGUI as sg


# DARK1 = "#171717"
# DARK2 = "#212121"
# DARK3 = "#292929"
#
# BG_COLOR = DARK1
# TEXT_COLOR = "#dedede"
#
# INPUT_COLOR = DARK2
# INPUT_TEXT_COLOR = "#f56f3b"
#
# BUTTON_BG_COLOR = DARK3
# BUTTON_FG_COLOR = "#f56f3b"
#
# SCROLL_BAR_COLOR = "#0d0d0d"
#
# PROGRESS_BAR_BG_COLOR = "#2e2e2e"
# PROGRESS_BAR_FG_COLOR = "#69b1d0"
#
# BORDER_THICKNESS = 1
# SLIDER_DEPTH = 1
# PROGRESS_DEPTH = 1

# THEME_DICT = {
#     "BACKGROUND": BG_COLOR,
#     "TEXT": TEXT_COLOR,
#     "INPUT": INPUT_COLOR,
#     "TEXT_INPUT": INPUT_TEXT_COLOR,
#     "SCROLL": SCROLL_BAR_COLOR,
#     "BUTTON": (BUTTON_FG_COLOR, BUTTON_BG_COLOR),
#     "PROGRESS": (PROGRESS_BAR_FG_COLOR, PROGRESS_BAR_BG_COLOR),
#     "BORDER": BORDER_THICKNESS,
#     "SLIDER_DEPTH": SLIDER_DEPTH,
#     "PROGRESS_DEPTH": PROGRESS_DEPTH
# }


THEME_NAME = "EPR Theme"


PALETTE = {
    "colors": {
        "dark1": "#171717",
        "dark2": "#212121",
        "dark3": "#292929",
        "light": "#dedede",
        "accent": "#f56f3b",
    },
    "thicknesses": {"border": "1"},
    "depths": {"slider": 0, "progress": 0}
}


THEME_DICT = {
    "BACKGROUND": PALETTE["colors"]["dark1"],
    "TEXT": PALETTE["colors"]["light"],
    "INPUT": PALETTE["colors"]["dark2"],
    "TEXT_INPUT": PALETTE["colors"]["accent"],
    "SCROLL": PALETTE["colors"]["dark2"],
    "BUTTON": (PALETTE["colors"]["accent"], PALETTE["colors"]["dark3"]),
    "PROGRESS": (PALETTE["colors"]["accent"], PALETTE["colors"]["dark3"]),
    "BORDER": PALETTE["thicknesses"]["border"],
    "SLIDER_DEPTH": PALETTE["depths"]["slider"],
    "PROGRESS_DEPTH": PALETTE["depths"]["progress"]
}


def create_epr_theme():
    sg.theme_add_new(THEME_NAME, THEME_DICT)
    sg.theme(THEME_NAME)
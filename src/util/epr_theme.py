import FreeSimpleGUI as sg


THEME_NAME = "EPR Theme"


PALETTE = {
    "colors": {
        # "dark1": "#171717",
        # "dark2": "#212121",
        # "dark3": "#292929",
        "dark1": "#1c1e23",
        "dark2": "#272a31",
        "dark3": "#313641",
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
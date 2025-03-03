import random
import FreeSimpleGUI as sg


class GuiManager:
    __WINDOW_TITLE = "EditorPerRepo"
    __DEFAULT_WINDOW_SIZE = (700, 300)
    __WINDOW_ALPHA = 0.98
    __WINDOW_ELEMENT_JUSTIFICATION = "center"
    __WINDOW_FINALIZE = True
    __WINDOW_RESIZABLE = False
    __AUTO_SIZE_BUTTONS = False
    __DEFAULT_BUTTON_SIZE = (12, 1)
    __AUTO_SIZE_TEXT = True
    __TEXT_JUSTIFICATION = "c"
    __FONT = ("Helvetica Neue Regular", 13)


    def __init__(self):
        themes = ['DarkGrey11', 'DarkGrey8']
        self.theme = themes[random.randrange(0, len(themes))]
        sg.theme(self.theme)
        print(sg.theme())


    def create_window(self):
        header_texts = [
            [sg.Text("It looks like you haven't assigned an editor to this repo yet!", key="-HEADER-")],
            [sg.Text("Please select one now.", key="-SUBHEADER-")]
        ]

        input_section = [
            sg.DropDown(values=["PyCharm", "Webstorm", "VSCode"], default_value="Webstorm",
                        key="-DROPDOWN-", pad=10, enable_events=True, readonly=True, expand_x=True),
            sg.Button("Submit", key="-SUBMIT-", pad=10, auto_size_button=False, size=(8, 1))
        ]

        layout = [
            [sg.Frame("frame1", [[sg.Text("BBBBBBBBB")]])],
            [sg.VStretch()],
            *header_texts,
            input_section,
            [sg.VStretch()],
        ]

        # layout = [
        #     [sg.Column(layout, vertical_alignment="c", element_justification="center", expand_y=True, expand_x=True)],
        # ]

        # print(layout)

        window = sg.Window(self.__WINDOW_TITLE,
                           layout,
                           size=self.__DEFAULT_WINDOW_SIZE,
                           alpha_channel=self.__WINDOW_ALPHA,
                           element_justification=self.__WINDOW_ELEMENT_JUSTIFICATION,
                           finalize=self.__WINDOW_FINALIZE,
                           resizable=self.__WINDOW_RESIZABLE,
                           auto_size_buttons=self.__AUTO_SIZE_BUTTONS,
                           default_button_element_size=self.__DEFAULT_BUTTON_SIZE,
                           auto_size_text=self.__AUTO_SIZE_TEXT,
                           text_justification=self.__TEXT_JUSTIFICATION,
                           element_padding=8,
                           font=self.__FONT)

        # while True:
        #     event, values = window.read()
        #
        #     if event in [sg.WIN_CLOSED, "Cancel", "Exit"]:
        #         break
        #
        #     if event == "-DROPDOWN-":
        #         print(event, values)
        #
        #     if event == "-SUBMIT-":
        #         print(event, values)


        # window.close()

        window.read()
        window.close()
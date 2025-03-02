import random
import FreeSimpleGUI as sg


class GuiManager:
    __WINDOW_TITLE = "EditorPerRepo"
    __DEFAULT_WINDOW_SIZE = (600, 350)
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


    def create_layout(self):
        header_texts = [
            [sg.Text("It looks like you haven't assigned an editor to this repo yet!", key="-HEADER-")],
            [sg.Text("Please select one now.", key="-SUBHEADER-")]
        ]

        # left_column_layout = [
        #     [sg.Text("Recently Used Editors:")],
        #     [sg.ButtonMenu("asdf", menu_def=["A","B"])],
        #     # [sg.Button("Editor 1")],
        #     # [sg.Button("Editor 1")],
        #     # [sg.Button("Editor 1")],
        #     # [sg.Button("Editor 1")],
        #     # [sg.Button("Editor 1")],
        #     # [sg.Button("Editor 1")]
        # ]

        # td = sg.TreeData()
        # td.insert("", "editor_1", "PyCharm", ["C:/Program Files/JetBrains/*/*/pycharm64.exe"])


        # left_column_layout = [
        #     [sg.Text("Recently Used Editors:")],
        #     [sg.Tree(td, ["Location"], expand_x=True, expand_y=True, auto_size_columns=False)]
        # ]

        # right_column_layout = [[sg.Text("Add an Editor:")]]


        return [
            header_texts,
            [sg.Table([["PyCharm", "C:/Program Files/JetBrains/*/*/pycharm64.exe"]],
                      headings=["Program", "Location"],
                      expand_x=True, expand_y=True, cols_justification="left", auto_size_columns=True,
                      # col_widths=[100, 20],
                      # def_col_width=10,
                      justification="left"
                      )]
            # [
            #     # [sg.Text("Recently Used Editors:")],
            #     # [sg.Tree(td, ["Location"], expand_x=True, expand_y=True, auto_size_columns=False)]
            # ]
            # left_column_layout
            # [
            #     *[sg.Column(layout,
            #                 background_color="red",
            #                 expand_x=True, expand_y=True,
            #                 element_justification="center")
            #       for layout in [left_column_layout, right_column_layout]]
            # ]
        ]


    def create_window(self):
        window = sg.Window(self.__WINDOW_TITLE,
                           self.create_layout(),
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

        window.read()
        window.close()
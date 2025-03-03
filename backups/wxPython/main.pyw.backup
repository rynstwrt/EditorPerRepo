import wx


class EPRFrame(wx.Frame):
    __WINDOW_TITLE = "EditorPerRepo"
    __DEFAULT_WINDOW_SIZE = (700, 400)

    __BG_COLOR = "#1d2125"
    __SURFACE_COLOR = "#2b3137"
    __TEXT_COLOR = "white"


    def __init__(self, *args, **kw):
        super(EPRFrame, self).__init__(*args, **kw)



        self.SetTitle(self.__WINDOW_TITLE)
        self.SetBackgroundColour(self.__BG_COLOR)
        self.SetInitialSize(wx.Size(*self.__DEFAULT_WINDOW_SIZE))
        self.CenterOnScreen()
        self.Fit()



        panel = wx.Panel(self)



        vert_sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(vert_sizer)



        header_text = wx.StaticText(panel, label=self.__WINDOW_TITLE, style=wx.ALIGN_CENTER)
        header_text.SetForegroundColour(self.__TEXT_COLOR)
        font: wx.Font = header_text.GetFont()
        font.SetPointSize(25)
        font.SetFaceName("Roboto")
        font.SetWeight(800)
        header_text.SetFont(font)

        vert_sizer.Add(header_text,
                       wx.SizerFlags()
                       .Expand()
                       .Align(wx.CENTER)
                       .Border(wx.TOP | wx.BOTTOM, 20))



        horiz_sizer = wx.BoxSizer(wx.HORIZONTAL)



        comboxbox = wx.ComboBox(panel,
                                choices=["test", "meme2", "asdfas"],
                                value="test",
                                style=wx.CB_READONLY | wx.CB_SORT)
        comboxbox.SetMinSize((300, 50))
        combo_font: wx.Font = comboxbox.GetFont()
        combo_font.SetPointSize(10)
        comboxbox.SetFont(combo_font)
        horiz_sizer.Add(comboxbox)


        add_button = wx.Button(panel)
        add_button.SetLabelText("+")
        horiz_sizer.Add(add_button)



        vert_sizer.Add(horiz_sizer, wx.SizerFlags().Align(wx.ALIGN_CENTER))

        # vert_sizer.Add(comboxbox, wx.SizerFlags().Align(wx.ALIGN_CENTER_HORIZONTAL))



        button = wx.Button(panel)
        button.SetLabelText("Submit")
        vert_sizer.Add(button, wx.SizerFlags().Align(wx.ALIGN_CENTER_HORIZONTAL))






if __name__ == "__main__":
    app = wx.App()

    frame = EPRFrame(None)
    frame.Show()

    app.MainLoop()
import wx
import wx.html


class EPRFrame(wx.Frame):
    __WINDOW_TITLE = "EditorPerRepo"
    __DEFAULT_WINDOW_SIZE = (700, 400)

    __BG_COLOR = "#1d2125"
    __SURFACE_COLOR = "#2b3137"
    __TEXT_COLOR = "white"


    def __init__(self, *args, **kw):
        super(EPRFrame, self).__init__(*args, **kw)



        self.SetTitle(self.__WINDOW_TITLE)
        # self.SetBackgroundColour(self.__BG_COLOR)
        self.SetInitialSize(wx.Size(*self.__DEFAULT_WINDOW_SIZE))
        self.CenterOnScreen()
        # self.Fit()


        html = wx.html.HtmlWindow(self)
        # html = wx.html.HtmlWindow(self, style=wx.DEFAULT_FRAME_STYLE)
        html.SetRelatedFrame(self, "HTML : %s")
        html.LoadFile("test.html")
        # html.LoadPage("test.html")






if __name__ == "__main__":
    app = wx.App()

    # frame = EPRFrame(None)
    # frame.Show()
    # app.SetTopWindow(frame)

    EPRFrame(None).Show()

    app.MainLoop()
import wx

app = None

class Size(wx.Frame):
    def __init__(self, parent, id, title):
        frame = wx.Frame.__init__(self, parent, id, title, size=(250, 200))
        w, h = 100, 100
        bmp = wx.EmptyBitmap(w, h)
        dc = wx.MemoryDC()
        dc.SelectObject(bmp)
        dc.Clear()
        text = "whatever"
        tw, th = dc.GetTextExtent(text)
        dc.DrawText(text, (w-tw)/2,  (h-th)/2)
        dc.SelectObject(wx.NullBitmap)
        wx.StaticBitmap(self, -1, bmp)
        self.Show(True)


app = wx.App()
Size(None, -1, 'Size')
app.MainLoop()
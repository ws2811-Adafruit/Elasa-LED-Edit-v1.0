import wx


class Smiley(wx.PyControl):
    def __init__(self, parent, size=(5,5)):
        super(Smiley, self).__init__(parent,
                                     size=size,
                                     style=wx.NO_BORDER)

        self.InitBuffer()                   # new
        self.Bind(wx.EVT_SIZE, self.OnSize) # new
        self.Bind(wx.EVT_IDLE, self.OnIdle) # new

        self.Bind(wx.EVT_PAINT, self.OnPaint)

# new block
    def InitBuffer(self):
        self.client_size = self.GetClientSize()
        self.buffer = wx.EmptyBitmap(self.client_size.width, self.client_size.height)
        dc = wx.BufferedDC(None, self.buffer)
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        self.DrawImage(dc)
        self.reInitBuffer = False

    def OnSize(self, event):
        self.reInitBuffer = True

    def OnIdle(self, event):
        if self.reInitBuffer:
            self.InitBuffer()
            self.Refresh(False)

    def DrawImage(self, dc):

        # Get the working rectangle we can draw in
        rect = self.client_size 

        # Find a square inside a rectangle (size of the client)
        min_side = min(rect.x, rect.y)
        rect.SetHeight(min_side)
        rect.SetWidth(min_side)

        # Setup the DC
        dc.SetPen(wx.BLACK_PEN) # for drawing lines / borders
        yellowbrush = wx.Brush(wx.Colour(255, 255, 0))
        dc.SetBrush(yellowbrush) # Yellow fill

        # Find the center and draw the circle
        cx = rect.width / 2
        cy = rect.width / 2
        radius = min(rect.width, rect.height) / 2
        dc.DrawCircle(cx, cy, radius)

        # Give it some square blue eyes
        # Calc the size of the eyes 1/8th total
        eyesz = (rect.width / 8, rect.height / 8)
        eyepos = (cx / 2, cy / 2)
        dc.SetBrush(wx.BLUE_BRUSH)
        dc.DrawRectangle(eyepos[0], eyepos[1],
                         eyesz[0], eyesz[1])
        eyepos = (eyepos[0] + (cx - eyesz[0]), eyepos[1])
        dc.DrawRectangle(eyepos[0], eyepos[1],
                         eyesz[0], eyesz[1])

        # Draw the smile
        dc.SetBrush(yellowbrush)
        startpos = (cx / 2, (cy / 2) + cy)
        endpos = (cx + startpos[0], startpos[1])
        dc.DrawArc(startpos[0], startpos[1],
                   endpos[0], endpos[1], cx, cy)

        # Draw a yellow rectangle to cover up the
        # unwanted black lines from the wedge part of
        # our arc
        dc.SetPen(wx.TRANSPARENT_PEN)
        dc.DrawRectangle(startpos[0], cy,
                         endpos[0] - startpos[0],
                         startpos[1] - cy)
# end of a new block

    def OnPaint(self, event):
        wx.BufferedPaintDC(self, self.buffer)


class SmileyApp(wx.App):
    def OnInit(self):
        self.frame = SmileyFrame(None,
                                 title="Drawing Shapes",
                                 size=(300,400))
        self.frame.Show()
        return True

class SmileyFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        wx.Frame.__init__(self, parent, *args, **kwargs)

        # Attributes
        self.panel = SmileyPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)

class SmileyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Layout
        self.__DoLayout()

    def __DoLayout(self):
        # Layout a grid of 4 smileys
        msizer = wx.GridSizer(2, 2, 0, 0)

        for x in range(4):
            smile = Smiley(self)
            msizer.Add(smile, 0, wx.EXPAND)

        self.SetSizer(msizer)

if __name__ == '__main__':
    app = SmileyApp(False)
    app.MainLoop()
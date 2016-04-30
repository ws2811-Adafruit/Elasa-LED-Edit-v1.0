import wxversion
# wxversion.select("2.8")
import wx
import wx.media

import itertools as IT
import os

IMAGE_DIR = os.path.expanduser('H:\ieee//all_functions\linux server\python GUI\Grid_on_photo/images')
SOUND_DIR = os.path.expanduser('H:\ieee//all_functions\linux server\python GUI\Grid_on_photo/sounds')


class MainWindow(wx.Frame):

    title = "Main Menu"

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Window', size=(1000, 700))
        panel = wx.Panel(self, -1)
        self.SetBackgroundColour(wx.Colour(100, 100, 100))
        self.Centre()
        self.Show()

        status = self.CreateStatusBar()

        menubar = wx.MenuBar()
        filemenu = wx.Menu()
        exitmenu = filemenu.Append(wx.NewId(), "Exit", "Exit Program")

        menubar.Append(filemenu, "File")
        self.Bind(wx.EVT_MENU, self.onExit, exitmenu)
        self.SetMenuBar(menubar)

        font1 = wx.Font(
            30, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')

        Text1 = wx.StaticText(panel, -1, "Rhythm Trainer", (10, 15))
        Text1.SetFont(font1)
        Text1.SetForegroundColour('white')

        btn1 = wx.Button(panel, label='Basic', pos=(100, 200), size=(150, 50))
        btn1.SetFont(
            wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, u'Consolas'))

        self.Bind(wx.EVT_BUTTON, self.newwindow, btn1)

        btn2 = wx.Button(
            panel, label='Advanced', pos=(100, 270), size=(150, 50))
        btn2.SetFont(
            wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, u'Consolas'))

        btn3 = wx.Button(
            panel, label='Notations', pos=(100, 340), size=(150, 50))
        btn3.SetFont(
            wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, u'Consolas'))

        btn4 = wx.Button(
            panel, label='Settings', pos=(100, 410), size=(150, 50))
        btn4.SetFont(
            wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, u'Consolas'))

        btn5 = wx.Button(panel, label="Quit", pos=(820, 550), size=(150, 50))
        btn5.SetFont(
            wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, u'Consolas'))
        self.Bind(wx.EVT_BUTTON, self.OnClick, btn5)

    def OnClick(self, event):
        self.Close()

    def OnQuitButton(self, event):
        wx.Sleep(1)
        self.Destroy()

    def onExit(self, event):
        self.Destroy()

    def newwindow(self, event):
        secondWindow = Window2(parent=None, id=-1)
        secondWindow.Show()
        self.Close()


class Window2(wx.Frame):

    title = "new Window"

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Window2', size=(1000, 700))
        panel = wx.Panel(self, -1)

        self.SetBackgroundColour(wx.Colour(100, 100, 100))
        self.Centre()
        self.Show()

        status = self.CreateStatusBar()

        menubar = wx.MenuBar()
        filemenu = wx.Menu()
        exitmenu = filemenu.Append(wx.NewId(), "Exit", "Exit Program")

        menubar.Append(filemenu, "File")
        self.Bind(wx.EVT_MENU, self.onExit, exitmenu)
        self.SetMenuBar(menubar)

        font2 = wx.Font(
            30, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')

        Text2 = wx.StaticText(panel, -1, "Rhythm Trainer", (10, 15))
        Text2.SetFont(font2)
        Text2.SetForegroundColour('white')
        self.Show(True)

        btn1 = wx.Button(panel, label="Back", pos=(820, 550), size=(150, 50))
        btn1.SetFont(
            wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, u'Consolas'))
        self.Bind(wx.EVT_BUTTON, self.OnClick, btn1)

        btn2 = wx.Button(panel, label="Play", pos=(820, 100), size=(150, 50))
        btn2.SetFont(
            wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, u'Consolas'))
        self.Bind(wx.EVT_BUTTON, self.onPlaySound, btn2)

        btn3 = wx.Button(panel, label="Stop", pos=(820, 150), size=(150, 50))
        btn3.SetFont(
            wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, u'Consolas'))
        self.Bind(wx.EVT_BUTTON, self.onStopSound, btn3)

        btn4 = wx.Button(panel, label="Next", pos=(820, 200), size=(150, 50))
        btn4.SetFont(
            wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, u'Consolas'))
        self.Bind(wx.EVT_BUTTON, self.loadImage, btn4)
        self.panel = wx.Panel(self, -1, pos=(50, 50), size=(800, 200))

        self.images = IT.cycle(
            [filename for filename in os.listdir(IMAGE_DIR)
             if any(filename.lower().endswith(ext) 
                    for ext in ('.png', '.jpg', '.jpeg'))])
        self.image_file = next(self.images)

        img = wx.EmptyImage(240,240)
        self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY, 
                                         wx.BitmapFromImage(img), pos=(200, 50))

    def loadImage(self, event):
        self.image_file = next(self.images)
        print(self.image_file)
        image_file = os.path.join(IMAGE_DIR, self.image_file)
        img = wx.Image(image_file, wx.BITMAP_TYPE_ANY)
        img = img.Scale(240,240)
        # The idea of using imageCtrl.SetBitmap comes from
        # http://www.blog.pythonlibrary.org/2010/03/26/creating-a-simple-photo-viewer-with-wxpython/
        self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))

    def onPlaySound(self, event):
        sound_file, ext = os.path.splitext(self.image_file)
        sound_file = os.path.join(SOUND_DIR, sound_file + '.mp3')
        print(sound_file)
        sound = wx.Sound(sound_file)
        # sound.IsOk(wx.SOUND_ASYNC)
        sound.Play(wx.SOUND_ASYNC)

    def onStopSound(self, event):
        wx.Sound.Stop()

    def onExit(self, event):
        self.Destroy()
        wx.Sound.Stop()

    def OnClick(self, event):
        wx.Sound.Stop()
        self.Close()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MainWindow(parent=None, id=-1)
    app.MainLoop()
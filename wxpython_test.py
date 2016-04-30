#!/usr/bin/python
# -*- coding: utf-8 -*-
import wx,os
# from wx import wxPySimpleApp, wxFrame
# from wx import button

image_address='C:\Users\Hamed\Pictures\LED\led.jpg'

# class LoginDialog(wx.Dialog):
#     def __init__(self, *args, **kwargs):
#         super(LoginDialog, self).__init__(*args, **kwargs)
#         # Attributes
#         self.panel = LoginPanel(self)
#         # Layout
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(self.panel, 1, wx.EXPAND)
#         self.SetSizer(sizer)
#         self.SetInitialSize()
#     def GetUsername(self):
#         return self.panel.GetUsername()
#     def GetPassword(self):
#         return self.panel.GetPassword()

def SetClipboardText(text):
    """Put text in the clipboard
    @param text: string
    """
    data_o = wx.TextDataObject()
    data_o.SetText(text)
    if wx.TheClipboard.IsOpened() or wx.TheClipboard.Open():
        wx.TheClipboard.SetData(data_o)
        wx.TheClipboard.Close()

def GetClipboardText():
    """Get text from the clipboard
    @return: string
    """
    text_obj = wx.TextDataObject()
    rtext = ""
    if wx.TheClipboard.IsOpened() or wx.TheClipboard.Open():
        if wx.TheClipboard.GetData(text_obj):
            rtext = text_obj.GetText()
        wx.TheClipboard.Close()
    return rtext

class FileAndTextDropTarget(wx.PyDropTarget):
    """Drop target capable of accepting dropped
    files and text
    """
    def __init__(self, file_callback, text_callback):
        assert callable(file_callback)
        assert callable(text_callback)
        super(FileAndTextDropTarget, self).__init__()
        # Attributes
        self.fcallback = file_callback # Drop File Callback
        self.tcallback = text_callback # Drop Text Callback
        self._data = None
        self.txtdo = None
        self.filedo = None
        # Setup
        self.InitObjects()
    def InitObjects(self):
        """Initializes the text and file data objects"""
        self._data = wx.DataObjectComposite()
        self.txtdo = wx.TextDataObject()
        self.filedo = wx.FileDataObject()
        self._data.Add(self.txtdo, False)
        self._data.Add(self.filedo, True)
        self.SetDataObject(self._data)
    def OnData(self, x_cord, y_cord, drag_result):
        """Called by the framework when data is dropped
        on the target
        """
        if self.GetData():
            data_format = self._data.GetReceivedFormat()
            if data_format.GetType() == wx.DF_FILENAME:
                self.fcallback(self.filedo.GetFilenames())
            else:
                self.tcallback(self.txtdo.GetText())
        return drag_result

class DropTargetFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="",
        pos=wx.DefaultPosition, size=wx.DefaultSize,
        style=wx.DEFAULT_FRAME_STYLE,
        name="DropTargetFrame"):
        super(DropTargetFrame, self).__init__(parent, id,
        title, pos,
        size, style,
        name)
        # Attributes
        choices = ["Drag and Drop Text or Files here",]
        self.list = wx.ListBox(self,
        choices=choices)
        self.dt = FileAndTextDropTarget(self.OnFileDrop,
        self.OnTextDrop)
        self.list.SetDropTarget(self.dt)
        # Setup
        self.CreateStatusBar()
    def OnFileDrop(self, files):
        self.PushStatusText("Files Dropped")
        for f in files:
            self.list.Append(f)
    def OnTextDrop(self, text):
        self.PushStatusText("Text Dropped")
        self.list.Append(text)

class LoginPanel(wx.Panel):
    def __init__(self, parent):
        super(LoginPanel, self).__init__(parent)
        # Attributes
        self._username = wx.TextCtrl(self)
        self._passwd = wx.TextCtrl(self, style=wx.TE_PASSWORD)
        # Layout
        sizer = wx.FlexGridSizer(2, 2, 8, 8)
        sizer.Add(wx.StaticText(self, label="Username:"),
        0, wx.ALIGN_CENTER_VERTICAL)
        sizer.Add(self._username, 0, wx.EXPAND)
        sizer.Add(wx.StaticText(self, label="Password:"),
        0, wx.ALIGN_CENTER_VERTICAL)
        sizer.Add(self._passwd, 0, wx.EXPAND)
        msizer = wx.BoxSizer(wx.VERTICAL)
        msizer.Add(sizer, 1, wx.EXPAND|wx.ALL, 20)
        btnszr = wx.StdDialogButtonSizer()
        button = wx.Button(self, wx.ID_OK)
        button.SetDefault()
        btnszr.AddButton(button)
        msizer.Add(btnszr, 0, wx.ALIGN_CENTER|wx.ALL, 12)
        btnszr.Realize()
        self.SetSizer(msizer)
    def GetUsername(self):
        return self._username.GetValue()
    def GetPassword(self):
        return self._passwd.GetValue()

class MyPopupMenu(wx.Menu):

    def __init__(self, parent):
        super(MyPopupMenu, self).__init__()

        self.parent = parent

        mmi = wx.MenuItem(self, wx.NewId(), 'Minimize')
        self.AppendItem(mmi)
        self.Bind(wx.EVT_MENU, self.OnMinimize, mmi)

        cmi = wx.MenuItem(self, wx.NewId(), 'Close')
        self.AppendItem(cmi)
        self.Bind(wx.EVT_MENU, self.OnClose, cmi)


    def OnMinimize(self, e):
        self.parent.Iconize()

    def OnClose(self, e):
        self.parent.Close()

class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="",
        pos=wx.DefaultPosition, size=wx.DefaultSize,
        style=wx.DEFAULT_FRAME_STYLE,
        name="MyFrame", *args, **kwargs):
        super(MyFrame, self).__init__(parent, id, title,
        pos, size, style, name)
        # Attributes
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.RED)
        self.button = wx.Button(self.panel,
        label="Push Me",
        pos=(50, 50))
        # self.btnId = wx.button.GetId()
        # Event Handlers
        button = wx.Button(self.panel,
        label="Get Children",
        pos=(50, 50))
        self.btnId = button.GetId()
        self.Bind(wx.EVT_BUTTON, self.OnButton,button)
        img_path = os.path.abspath(image_address)
        bitmap = wx.Bitmap(img_path, type=wx.BITMAP_TYPE_JPEG)
        self.bitmap = wx.StaticBitmap(self.panel,
        bitmap=bitmap)

        # Setup
        path = os.path.abspath(image_address)
        icon = wx.Icon(path, wx.BITMAP_TYPE_JPEG)
        self.SetIcon(icon)


        # Setup
        ok_btn = wx.Button(self.panel, wx.ID_OK)
        cancel_btn = wx.Button(self.panel, wx.ID_CANCEL,
        pos=(100, 0))
        menu_bar = wx.MenuBar()
        edit_menu = wx.Menu()
        edit_menu.Append(wx.NewId(), "Test")
        edit_menu.Append(wx.ID_PREFERENCES)
        menu_bar.Append(edit_menu, "Edit")
        self.SetMenuBar(menu_bar)

        APP_EXIT = 1
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW, '&New')
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.AppendSeparator()


        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import newsfeed list...')
        imp.Append(wx.ID_ANY, 'Import bookmarks...')
        imp.Append(wx.ID_ANY, 'Import mail...')

        fileMenu.AppendMenu(wx.ID_ANY, 'I&mport', imp)

        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.AppendItem(qmi)
        # qmi.SetBitmap(wx.Bitmap(image_address))

        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)



        fileMenu = wx.Menu()
        viewMenu = wx.Menu()

        self.shst = viewMenu.Append(wx.ID_ANY, 'Show statubar',
            'Show Statusbar', kind=wx.ITEM_CHECK)
        self.shtl = viewMenu.Append(wx.ID_ANY, 'Show toolbar',
            'Show Toolbar', kind=wx.ITEM_CHECK)

        viewMenu.Check(self.shst.GetId(), True)
        viewMenu.Check(self.shtl.GetId(), True)

        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)
        self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.shtl)

        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

        # menubar.Append(fileMenu, '&File')
        menubar.Append(viewMenu, '&View')
        self.SetMenuBar(menubar)


        vbox = wx.BoxSizer(wx.VERTICAL)

        toolbar1 = wx.ToolBar(self)
        # toolbar1.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('tnew.png'))
        # toolbar1.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('topen.png'))
        # toolbar1.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('tsave.png'))
        # toolbar1.Realize()
        #
        # toolbar2 = wx.ToolBar(self)
        # qtool = toolbar2.AddLabelTool(wx.ID_EXIT, '', wx.Bitmap("E:\soheil\web_site_root\ieee\\"+"all_functions\linux server\python GUI\\"+'bag-Logo.png'))
        # toolbar2.Realize()
        #
        # vbox.Add(toolbar1, 0, wx.EXPAND)
        # vbox.Add(toolbar2, 0, wx.EXPAND)
        #
        # self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)
        #
        # self.SetSizer(vbox)

        self.toolbar = self.CreateToolBar()
        self.toolbar.AddLabelTool(1, '', wx.Bitmap('C:\Users\Hamed\Documents\soheil sites image\\'+'4300888.png'))
        self.toolbar.Realize()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')

        self.SetSize((350, 250))
        self.SetTitle('Check menu item')
        self.Centre()
        self.Show(True)

    def OnRightDown(self, e):
        self.PopupMenu(MyPopupMenu(self), e.GetPosition())

    def ToggleStatusBar(self, e):

        if self.shst.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()

    def ToggleToolBar(self, e):

        if self.shtl.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()

    def OnQuit(self, e):
        self.Close()
        # pre = wx.PreFrame()
        # pre.SetExtraStyle(wx.FRAME_EX_CONTEXTHELP)
        # pre.Create(parent, *args, **kwargs)
        # self.PostCreate(pre)
        # self.frame = LoginPanel(None)
        # self.SetTopWindow(self.frame)
        # self.frame.Show()

    def OnButton(self, event):
        """Called when the Button is clicked"""
        print "\nFrame GetChildren:"
        for child in self.GetChildren():
            print "%s" % repr(child)
        print "\nPanel FindWindowById:"
        button = self.panel.FindWindowById(self.btnId)
        print "%s" % repr(button)
        # Change the Button's label
        button.SetLabel("Changed Label")
        print "\nButton GetParent:"
        panel = button.GetParent()
        print "%s" % repr(panel)
        print "\nGet the Application Object:"
        app = wx.GetApp()
        print "%s" % repr(app)
        print "\nGet the Frame from the App:"
        frame = app.GetTopWindow()
        print "%s" % repr(frame)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="The Main Frame")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        # wx.MessageBox("Hello wxPython", "wxApp")
        # LoginDialog()
        GetClipboardText()

        # FileAndTextDropTarget()
        DropTargetFrame(None)
        return True
if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
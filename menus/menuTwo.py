import wx

########################################################################
class MyForm(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="wx.Menu Tutorial")
        
        self.panel = wx.Panel(self, wx.ID_ANY)
 
        # create the menubar
        menuBar = wx.MenuBar()
        
        # create the first menu (starting on left)
        carMenu = wx.Menu()
        carMenu.Append(101, "&Ford", "An American Automaker")
        carMenu.Append(102, "&Nissan", "")
        carMenu.Append(103, "&Toyota", "Buy Japanese!")
        carMenu.Append(104, "&Close", "Close the application")
        
        # add a picture to a menu
        picMenu = wx.Menu()
        item = wx.MenuItem(picMenu, wx.ID_ANY, "Snake", "This menu has a picture!")
        img = wx.Image('snake32.bmp', wx.BITMAP_TYPE_ANY)
        item.SetBitmap(wx.BitmapFromImage(img))
        picMenu.AppendItem(item)
        
        # add menus to menubar
        menuBar.Append(carMenu, "&Vehicles")
        menuBar.Append(picMenu, "&Picture")
        self.SetMenuBar(menuBar)
        
    #----------------------------------------------------------------------
    def onExit(self, event):
        """"""
        self.Close()
        
#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()

    
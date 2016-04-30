# submenu.py
import wx

########################################################################
class MyForm(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="wx.Menu Tutorial")
        
        self.panel = wx.Panel(self, wx.ID_ANY)
 
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        openMenuItem = fileMenu.Append(wx.NewId(), "Open")
        
        # create a submenu
        subMenu = wx.Menu()
        historyMenuItem = subMenu.Append(wx.NewId(), "Show History")
        fileMenu.AppendMenu(wx.NewId(), "History", subMenu)
        
        exitMenuItem = fileMenu.Append(wx.NewId(), "Exit",
                                       "Exit the application")
        menuBar.Append(fileMenu, "&File")
        self.Bind(wx.EVT_MENU, self.onExit, exitMenuItem)
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
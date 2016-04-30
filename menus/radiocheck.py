# radiocheck.py
import wx
from wx.lib.flashwin import FlashWindow
########################################################################
class MyForm(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="wx.Menu Tutorial")
        
        self.panel = wx.Panel(self, wx.ID_ANY)
 
        # Create menu bar
        menuBar = wx.MenuBar()
        
        # Create radio menu
        radioMenu = wx.Menu()
        idleItem = radioMenu.Append(wx.NewId(), "IDLE",
                                   "a Python shell using tcl/tk as GUI",
                                   wx.ITEM_RADIO)
        pyCrustItem = radioMenu.Append(wx.NewId(),"PyCrust", 
                                      "a Python shell using wxPython as GUI",
                                      wx.ITEM_RADIO)
        psiItem = radioMenu.Append(wx.NewId(), "psi",
                                  "a simple Python shell using wxPython as GUI",
                                  wx.ITEM_RADIO)
        menuBar.Append(radioMenu, "&Radio")
        
        # create check menu
        checkMenu = wx.Menu()
        wgItem = checkMenu.Append(wx.NewId(), "Wells Fargo", "", wx.ITEM_CHECK)
        citiItem = checkMenu.Append(wx.NewId(), "Citibank", "", wx.ITEM_CHECK)
        geItem = checkMenu.Append(wx.NewId(), "GE Money Bank", "", wx.ITEM_CHECK)
        menuBar.Append(checkMenu, "&Check")
        
        # Attach menu bar to frame
        self.SetMenuBar(menuBar)
        
#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()
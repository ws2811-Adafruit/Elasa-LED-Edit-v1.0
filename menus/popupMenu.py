# submenu.py
import wx

########################################################################
class MyForm(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Popup Menu Tutorial")
        
        panel = wx.Panel(self, wx.ID_ANY)
 
        lbl = wx.StaticText(panel, label="Right click anywhere!")
        self.Bind(wx.EVT_CONTEXT_MENU, self.onContext)
        
    #----------------------------------------------------------------------
    def onContext(self, event):
        """
        Create and show a Context Menu
        """
        
        # only do this part the first time so the events are only bound once 
        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            self.itemTwoId = wx.NewId()
            self.itemThreeId = wx.NewId()
            self.Bind(wx.EVT_MENU, self.onPopup, id=self.popupID1)
            self.Bind(wx.EVT_MENU, self.onPopup, id=self.itemTwoId)
            self.Bind(wx.EVT_MENU, self.onExit, id=self.itemThreeId)
        
        # build the menu
        menu = wx.Menu()
        itemOne = menu.Append(self.popupID1, "ItemOne")
        itemTwo = menu.Append(self.itemTwoId, "ItemTwo")
        itemThree = menu.Append(self.itemThreeId, "Exit")
        
        # show the popup menu
        self.PopupMenu(menu)
        menu.Destroy()
                 
    #----------------------------------------------------------------------
    def onExit(self, event):
        """
        Exit program
        """
        self.Close()
        
    #----------------------------------------------------------------------
    def onPopup(self, event):
        """
        Print the label of the menu item selected
        """
        itemId = event.GetId()
        menu = event.GetEventObject()
        menuItem = menu.FindItemById(itemId)
        print menuItem.GetLabel()
        
#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()
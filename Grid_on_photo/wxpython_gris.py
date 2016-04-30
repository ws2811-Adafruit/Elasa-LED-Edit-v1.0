import wx

class FadeMixin(object):
    ''' FadeMixin provides one public method: DeleteItem. It is meant to
    be mixed in with a ListCtrl to 'fade out' items before they are
    really deleted. Mixin like this:

    Assumption: the background colour of the control is wx.WHITE

    class MyListCtrl(FadeMixin, wx.ListCtrl):
        ...
    '''
    def __init__(self, *args, **kwargs):
        self.__bgColour = wx.WHITE
        super(FadeMixin, self).__init__(*args, **kwargs)

    def DeleteItem(self, index, fadeStep=10, fadeSpeed=50):
        if self.IsEnabled():
            self.__startDeleteItem(index)
        fgColour, bgColour, transparentColour = self.__getColours(index)
        if fgColour == bgColour == transparentColour:
            self.__finishDeleteItem(index)
        else:
            for colour, setColour in [(fgColour, self.SetItemTextColour), 
                                      (bgColour, self.SetItemBackgroundColour)]:
                fadedColour = self.__fadeColour(colour, transparentColour, 
                                                fadeStep)
                setColour(index, fadedColour)
            wx.FutureCall(50, self.DeleteItem, index, fadeStep, fadeSpeed)

    def SetBackgroundColour(self, colour):
        self.__bgColour = colour
        super(FadeMixin, self).SetBackgroundColour(colour)

    def GetBackgroundColour(self):
        return self.__bgColour

    def __startDeleteItem(self, index):
        # Prevent user input during deletion. Things could get messy if
        # the user deletes another item when we're still busy fading out the 
        # first one:
        self.Disable()
        # Unselect the item that is to be deleted to make the fading visible:
        currentState = self.GetItemState(index, wx.LIST_STATE_SELECTED)
        self.SetItemState(index, ~currentState, wx.LIST_STATE_SELECTED)

    def __finishDeleteItem(self, index):
        super(FadeMixin, self).DeleteItem(index)
        self.Enable()

    def __getColours(self, index):
        fgColour = self.GetItemTextColour(index)
        bgColour = self.GetItemBackgroundColour(index)
        transparentColour = self.GetBackgroundColour()
        if not bgColour:
            bgColour = transparentColour
        return fgColour, bgColour, transparentColour

    def __fadeColour(self, colour, transparentColour, fadeStep):
        newColour = []
        for GetIntensity in wx.Colour.Red, wx.Colour.Green, wx.Colour.Blue:
            currentIntensity = GetIntensity(colour) 
            transparentIntensity = GetIntensity(transparentColour)
            if currentIntensity < transparentIntensity:
                newIntensity = min(transparentIntensity,
                                   currentIntensity + fadeStep)
            elif currentIntensity > transparentIntensity:
                newIntensity = max(transparentIntensity, 
                                currentIntensity - fadeStep)
            else:
                newIntensity = transparentIntensity
            newColour.append(newIntensity)
        return wx.Colour(*newColour)


class ListCtrl(FadeMixin, wx.ListCtrl):
    pass


class Frame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Frame, self).__init__(*args, **kwargs)
        self.list = ListCtrl(self, style=wx.LC_REPORT)
        self.list.InsertColumn(0, 'Column 0')
        self.list.InsertColumn(1, 'Column 1')
        self.fillList()
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelected)
        self.Bind(wx.EVT_LIST_DELETE_ITEM, self.onDeleted)

    def onSelected(self, event):
        self.list.DeleteItem(event.GetIndex())

    def onDeleted(self, event):
        if self.list.GetItemCount() == 1:
            wx.CallAfter(self.fillList, False)

    def fillList(self, firstTime=True):
        for row in range(10):
            self.list.InsertStringItem(row, 'ssItem %d, Column 0'%row)
            self.list.SetStringItem(row, 1, 'Item %d, Column 1'%row)
        self.list.SetItemBackgroundColour(1, wx.BLUE)
        self.list.SetItemTextColour(2, wx.BLUE)
        self.list.SetItemBackgroundColour(3, wx.GREEN)
        self.list.SetItemTextColour(4, wx.GREEN)
        self.list.SetItemBackgroundColour(5, wx.RED)
        self.list.SetItemTextColour(6, wx.RED)
        self.list.SetItemBackgroundColour(7, wx.BLACK)
        self.list.SetItemTextColour(7, wx.WHITE)
        self.list.SetItemBackgroundColour(8, wx.WHITE)
        self.list.SetItemTextColour(8, wx.BLACK)
        if not firstTime:
            self.list.SetBackgroundColour(wx.BLUE)


app = wx.App(False)
frame = Frame(None, title='Select an item to fade it out')
frame.Show()
app.MainLoop()
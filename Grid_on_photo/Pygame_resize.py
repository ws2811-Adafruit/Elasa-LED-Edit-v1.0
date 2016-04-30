import wx
import pygame

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

pygame.font.init()
try:
    regular_font_file = os.path.join(os.path.dirname(__file__), "Vera.ttf")
    bold_font_file = os.path.join(os.path.dirname(__file__), "VeraBd.ttf")

    # Check for cx_Freeze
    #
    if "frozen" in sys.__dict__.keys() and sys.frozen:

        regular_font_file = os.path.join(sys.path[1], "Vera.ttf")
        bold_font_file = os.path.join(sys.path[1], "VeraBd.ttf")

    BIG_FONT = pygame.font.Font(regular_font_file, 30)
    SMALL_FONT = pygame.font.Font(regular_font_file, 12)
    BOLD_FONT = pygame.font.Font(bold_font_file, 12)

except:
    # TODO: log used font: pygame.font.get_default_font()
    #print("Could not load {0}".format(os.path.join(os.path.dirname(__file__), "Vera.ttf")))
    BIG_FONT = pygame.font.Font(None, 40)
    SMALL_FONT = BOLD_FONT = pygame.font.Font(None, 20)


class PyGamePseudoImage():
    def __init__(self, size, color):
        self.screen = pygame.Surface(size, 0, 32)
        self.screen.fill(color)

    def getImage(self):
        return self.screen

class __MouseMixin:

    def onLeftUp(self, event):
        pass

    def onLeftDown(self, event):
        pass

    def onLeftDClick(self, event):
        pass

    def onRightUp(self, event):
        pass

    def onRightDown(self, event):
        pass

    def onDragging(self, event):
        pass

    def onMouseEnter(self, event):
        pass

    def OnMouseHandler(self, event):
        event.Skip()

        if event.LeftUp():
            self.onLeftUp(event)
        elif event.LeftDown():
            self.onLeftDown(event)
        elif event.LeftDClick():
            self.onLeftDClick(event)
        elif event.RightUp():
            self.onRightUp(event)
        elif event.RightDown():
            self.onRightDown(event)
        elif event.Dragging() and event.LeftIsDown():
            self.onDragging(event)

        pass


class DragSprite(__MouseMixin, pygame.sprite.Sprite):
    SPRITE_BUTTON, SPRITE_TRANSPORTER = range(2)

    def __init__(self, parent=None):
        pygame.sprite.Sprite.__init__(self)
        self.is_select = 0
        self.lastPos = 0
        self.lastUpdate = 0
        self.parent = parent

    def setLastPos(self, pos):
        self.lastPos = pos

    def move(self, pos):
        dx = pos[0] - self.lastPos[0]
        dy = pos[1] - self.lastPos[1]
        self.lastPos = pos
        center = (self.rect.center[0] + dx, self.rect.center[1] + dy)
        self.rect.center = center
        return

    def isSelected(self):
        return self.is_select

    def setSelect(self, is_select):
        self.is_select = is_select
        return

    def update(self, current_time):
        return

def drawBoader(image, rect):
    W,H = (rect.width, rect.height)
    yellow = (255, 255, 0)
    pygame.draw.rect(image, yellow, (0,0,W-2,H-2), 2)

class ButtonSprite(DragSprite):
    def __init__(self, parent=None, initPos=(0,0), width=50, height=50, dicts=None):
        DragSprite.__init__(self, parent)
        self.type = DragSprite.SPRITE_BUTTON
        self.resourceCfgDict = dicts
        self.imageResource = {}
        self.status = 0
        self.index = 0

        self.parent = parent
        self.initPos = (initPos[0], initPos[1])
        self.width = width
        self.height = height
        self.rectOnLoad = pygame.Rect(initPos, (width, height))
        self.rect = self.rectOnLoad.copy()

        self.operationOn = None
        self.operationOff = None

        self.operationDic = {"on": self.getOperationOnItem, "off": self.getOperationOffItem}
        self.guiCfg = None

        for dic in dicts:
            self.loadImgResource(dic)

        self.setCurrentResource("off")

    def getOperationOnItem(self):
        return self.operationOn

    def getOperationOffItem(self):
        return self.operationOff

    def loadImgResource(self, dict):
        """
            load image with pygame lib
        """
        key = dict[0]
        file_name = dict[1]

        #image_file = pygame.image.load(file_name) #use this to load real image
        image_file = PyGamePseudoImage((500,500), file_name).getImage()
        imagedata = pygame.image.tostring(image_file, "RGBA")
        imagesize = image_file.get_size()
        imageSurface = pygame.image.fromstring(imagedata, imagesize , "RGBA")

        self.imageResource[key] = (file_name, imageSurface)

    def resizeResource(self, src, size):
        return pygame.transform.smoothscale(src, size)

    def setCurrentResource(self, status):
        self.currentStatus = status
        self.imageOnLoad = self.resizeResource(self.imageResource[status][1], (self.width, self.height))
        self.image = pygame.transform.scale(self.imageOnLoad, (self.rect.width, self.rect.height))

    def switchResource(self, index):
        self.setCurrentResource(index)

    def onZoomUpdate(self, zoomRatio):
        parentRect = pygame.Rect(self.parent.GetRect())
        dx = self.rectOnLoad.centerx - parentRect.centerx
        dy = self.rectOnLoad.centery - parentRect.centery

        self.rect.centerx = parentRect.centerx + dx*zoomRatio
        self.rect.centery = parentRect.centery + dy*zoomRatio

        self.rect.height = self.imageOnLoad.get_rect().height * zoomRatio
        self.rect.width = self.imageOnLoad.get_rect().width * zoomRatio

        self.image = pygame.transform.scale(self.imageOnLoad, (self.rect.width, self.rect.height))

    def update(self, current_time, ratio):
        if self.isSelected():
            drawBoader(self.image, self.image.get_rect())
        else:
            pass
            #self.image = self.imageOnLoad.copy()

    def onRightUp(self, event):
        print "onRightUp"
        event.Skip(False)
        pass

    def onLeftDClick(self, event):
        if self.currentStatus == "on":
            self.setCurrentResource("off")
        elif self.currentStatus == "off":
            self.setCurrentResource("on")

        return

    def move(self, pos):
        DragSprite.move(self, pos)

        parentRect = pygame.Rect(self.parent.GetRect())
        centerDx = self.rect.centerx - parentRect.centerx
        centerDy = self.rect.centery - parentRect.centery

        self.rectOnLoad.centerx = parentRect.centerx + centerDx/self.parent.zoomRatio
        self.rectOnLoad.centery = parentRect.centery + centerDy/self.parent.zoomRatio


class MyHmiPanel(wx.Panel):
    def __init__(self, parent, ID):
        wx.Window.__init__(self, parent, ID)
        self.parent = parent
        self.hwnd = self.GetHandle()
        self.size = self.GetSizeTuple()
        self.size_dirty = True
        self.rootSpriteGroup = pygame.sprite.LayeredUpdates()

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_TIMER, self.Update, self.timer)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.fps = 60.0
        self.timespacing = 1000.0 / self.fps
        self.timer.Start(self.timespacing, False)
        self.previous_time = 0
        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouse)

        self.selectedSprite = None

        self.zoomRatio = 1
        self.background = None
        self.bgRect = None
        self.backgroundOnUpdate = None
        self.bgRetOnUpdate = None

        self.loadBackground()
        self.addTestSprite()

    def loadBackground(self):
        #self.background = pygame.image.load(image_file) #use this to load real image
        self.background = PyGamePseudoImage((500,500), (255, 0, 0)).getImage()
        self.bgRect = self.background.get_rect()
        self.backgroundOnUpdate = self.background.copy()
        self.bgRetOnUpdate = self.bgRect.copy()

    def resizeUpdateBackground(self):
        self.bgRect.center = self.screen.get_rect().center
        self.bgRetOnUpdate = self.bgRect.copy()

    def zoomUpdateBackground(self, zoomRatio):
        self.bgRetOnUpdate.width = self.bgRect.width * zoomRatio
        self.bgRetOnUpdate.height = self.bgRect.height * zoomRatio
        self.bgRetOnUpdate.width = self.bgRect.width * zoomRatio
        self.bgRetOnUpdate.center = self.screen.get_rect().center
        self.backgroundOnUpdate = pygame.transform.scale(self.background, (self.bgRetOnUpdate.width, self.bgRetOnUpdate.height))

    def drawBackground(self, screen):
        screen.blit(self.backgroundOnUpdate, self.bgRetOnUpdate)

    def addTestSprite(self):
        #self.rootSpriteGroup.add(ButtonSprite(self, initPos=(100, 100), width=100, height=100, dicts= [('on', btn_red_on), ('off', btn_red_off)]))
        #self.rootSpriteGroup.add(ButtonSprite(self, initPos=(200, 200), width=100, height=100, dicts= [('on', btn_red_on), ('off', btn_red_off)]))
        self.rootSpriteGroup.add(ButtonSprite(self, initPos=(100, 100), width=100, height=100, dicts= [('on', GREEN), ('off', BLUE)]))
        self.rootSpriteGroup.add(ButtonSprite(self, initPos=(200, 200), width=100, height=100, dicts= [('on', GREEN), ('off', BLUE)]))

    def Update(self, event):
        self.Redraw()
        return

    def Redraw(self):
        if  self.size[0] == 0  or  self.size[1] == 0:
            return

        if self.size_dirty:
            self.screen = pygame.Surface(self.size, 0, 32)
            self.resizeUpdateBackground()
            self.size_dirty = False

        self.screen.fill((0,0,0))
        self.drawBackground(self.screen)

        w, h = self.screen.get_size()
        current_time = pygame.time.get_ticks()

        self.previous_time = current_time
        self.rootSpriteGroup.update(current_time, self.zoomRatio)
        self.rootSpriteGroup.draw(self.screen)

        s = pygame.image.tostring(self.screen, 'RGB')  # Convert the surface to an RGB string
        #img = wx.ImageFromData(self.size[0], self.size[1], s)  # Load this string into a wx image
        img = wx.ImageFromData(w, h, s)  # Load this string into a wx image

        #if img.IsOk() is not True:
           # return
        bmp = wx.BitmapFromImage(img)  # Get the image in bitmap form
        dc = wx.ClientDC(self)  # Device context for drawing the bitmap
        dc = wx.BufferedDC( dc)
        dc.DrawBitmap(bmp, 0, 0, 1)  # Blit the bitmap image to the display


    def checkCollide(self, event):
        x , y = (event.GetX(),event.GetY())

        mousePoint = pygame.sprite.Sprite()
        mousePoint.rect = pygame.Rect(x, y, 1, 1)
        copoint = pygame.sprite.spritecollide(mousePoint, self.rootSpriteGroup, None)

        if copoint:
            copoint = copoint[-1]

        return copoint

    def removeSelectedSprite(self):
        if self.selectedSprite:
            self.selectedSprite.setSelect(0)
            self.selectedSprite = None

    def setNewSelectedSprite(self, sprite):
        self.removeSelectedSprite()
        sprite.setSelect(1)
        self.selectedSprite = sprite

    def onSelectSprite(self, event, onMouseObj):
        if onMouseObj:
            if self.selectedSprite:
                if onMouseObj != self.selectedSprite:
                    self.setNewSelectedSprite(onMouseObj)
            else:
                self.setNewSelectedSprite(onMouseObj)

            self.selectedSprite.setLastPos((event.GetX(),event.GetY()))
        else:
            self.removeSelectedSprite()

    def OnMouse(self, event):
        onMouseObj = self.checkCollide(event)
        event.Skip()

        if onMouseObj:
            onMouseObj.OnMouseHandler(event)

        if not event.GetSkipped():
            print "event dropped "
            return

        if event.LeftDown():
            self.onSelectSprite(event, onMouseObj)
        elif event.LeftUp():
            pass
        elif event.RightUp():
            self.onSelectSprite(event, onMouseObj)
        elif event.RightDown():
            self.onSelectSprite(event, onMouseObj)
        elif event.Dragging() and event.LeftIsDown():
            if self.selectedSprite:
                self.selectedSprite.move((event.GetX(),event.GetY()))

    def OnPaint(self, event):
        self.Redraw()
        event.Skip()  # Make sure the parent frame gets told to redraw as well

    def OnSize(self, event):
        self.size = self.GetSizeTuple()
        self.size_dirty = True

    def Kill(self, event):
        self.Unbind(event=wx.EVT_PAINT, handler=self.OnPaint)
        self.Unbind(event=wx.EVT_TIMER, handler=self.Update, source=self.timer)

    def onZoomIn(self):
        self.zoomRatio += 0.2
        self.onZoomUpdate()

    def onZoomReset(self):
        self.zoomRatio = 1
        self.onZoomUpdate()

    def onZoomOut(self):
        if self.zoomRatio > 0.2:
            self.zoomRatio -= 0.2
        self.onZoomUpdate()

    def onZoomUpdate(self):
        self.zoomUpdateBackground(self.zoomRatio)
        for s in self.rootSpriteGroup.sprites():
            s.onZoomUpdate(self.zoomRatio)


class TestFrame ( wx.Frame ):
    def __init__( self, parent, fSize ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = fSize, style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        fgSizer1 = wx.FlexGridSizer( 2, 1, 0, 0 )
        fgSizer1.AddGrowableCol( 0 )
        fgSizer1.AddGrowableRow( 0 )
        fgSizer1.SetFlexibleDirection( wx.VERTICAL )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )


        self.panelMain = MyHmiPanel(self, -1)

        fgSizer1.Add( self.panelMain, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.bZoomIn = wx.Button( self.m_panel4, wx.ID_ANY, u"Zoom In", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.bZoomIn, 0, wx.ALL, 5 )

        self.bReset = wx.Button( self.m_panel4, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.bReset, 0, wx.ALL, 5 )

        self.bZoomOut = wx.Button( self.m_panel4, wx.ID_ANY, u"Zoom Out", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.bZoomOut, 0, wx.ALL, 5 )

        self.m_panel4.SetSizer( bSizer3 )
        self.m_panel4.Layout()
        bSizer3.Fit( self.m_panel4 )
        fgSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )

        self.SetSizer( fgSizer1 )
        self.Layout()
        self.Centre( wx.BOTH )

        self.bZoomIn.Bind( wx.EVT_BUTTON, self.onZoomIn )
        self.bReset.Bind( wx.EVT_BUTTON, self.onZoomReset )
        self.bZoomOut.Bind( wx.EVT_BUTTON, self.onZoomOut )

    def __del__( self ):
        pass

    def onZoomIn( self, event ):
        self.panelMain.onZoomIn()
        event.Skip()

    def onZoomReset( self, event ):
        self.panelMain.onZoomReset()
        event.Skip()

    def onZoomOut( self, event ):
        self.panelMain.onZoomOut()
        event.Skip()


if __name__=='__main__':
        app = wx.App(redirect=False)
        frame = TestFrame(None, (800, 600))
        frame.SetPosition((100, 100))
        frame.Show()
        app.MainLoop()
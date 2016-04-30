
import ImageGrab
img = ImageGrab.grab()
img.save('test.jpg','JPEG')

import pyscreenshot as ImageGrab

# fullscreen
im=ImageGrab.grab()
im.show()

# part of the screen
im=ImageGrab.grab(bbox=(10,10,500,500))
im.show()

# to file
ImageGrab.grab_to_file('im.png')

import wx
wx.App()  # Need to create an App instance before doing anything
screen = wx.ScreenDC()
size = screen.GetSize()
bmp = wx.EmptyBitmap(size[0], size[1])
mem = wx.MemoryDC(bmp)
mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
del mem  # Release bitmap
bmp.SaveFile('screenshot.png', wx.BITMAP_TYPE_PNG)
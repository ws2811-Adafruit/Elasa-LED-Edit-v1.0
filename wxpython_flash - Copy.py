"""
GrooveWalrus: Flash Player
Copyright (C) 2009, 2010
11y3y3y3y43@gmail.com
http://groove-walrus.turnip-town.net
-----
This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation; either version 2 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program; if not, write to the Free Software Foundation, Inc., 59 Temple
Place, Suite 330, Boston, MA 02111-1307 USA
"""

#import urllib
#import urllib2

import wx
import wx.xrc as xrc
import os
from main_utils.read_write_xml import xml_utils
from main_utils import system_files
from main_utils import jiwa
#FLASH_ENABLED = True
try:
    from main_utils import player_flash
except Exception, expt:
    print "Flash plugin: "+ str(Exception) + str(expt)
    #FLASH_ENABLED = False    
#from wx.lib.flashwin import FlashWindow

#SYSLOC = os.path.abspath(os.path.dirname(sys.argv[0]))
#DIZZLER_SETTINGS = os.path.join(os.getcwd(), 'plugins','flash') + os.sep + "settings_flash.xml"
#DIZZLER = os.path.join(os.getcwd(), 'plugins','flash') + os.sep
DIZZLER_URL = 'http://www.dizzler.com/player/podmini.swf?m='
GROOVESHARK_URL ="http://listen.grooveshark.com/songWidget.swf?hostname=cowbell.grooveshark.com&style=metal&p=1&songID="
RESFILE = os.path.join(os.getcwd(), 'plugins','flash') + os.sep + "layout_flash.xml"
#http://www.dizzler.com/player/podmini.swf?m=chairlift-bruises
#http://www.boostermp3.com
#http://www.jiwa.fm
#http://www.jiwa.fm/res/widget/monotitle.swf?trackId=369589&skin=round
#http://www.jiwa.fr/track/search/q=u2%20one&noRestricted=true

class MainPanel(wx.Dialog):
    def __init__(self, parent, pathToPlugins=None):
        if(not pathToPlugins==None):
            RESFILE = os.path.join(pathToPlugins,'flash') + os.sep + "layout_flash.xml"
            
        wx.Dialog.__init__(self, parent, -1, "Flash", size=(475,310), style=wx.FRAME_SHAPED|wx.RESIZE_BORDER) #STAY_ON_TOP)        
        self.parent = parent
        
        self.FLASH_SETTINGS = system_files.GetDirectories(self).MakeDataDirectory('plugins') + os.sep
        
        # XML Resources can be loaded from a file like this:
        res = xrc.XmlResource(RESFILE)

        # Now create a panel from the resource data
        panel = res.LoadPanel(self, "m_pa_plugin_flash")

        # control references --------------------
        self.pa_flash_player = xrc.XRCCTRL(self, 'm_pa_flash_player')
        #header for dragging and moving
        self.st_flash_header = xrc.XRCCTRL(self, 'm_st_flash_header')        
        self.bm_flash_close = xrc.XRCCTRL(self, 'm_bm_flash_close')
        self.bm_flash_tab = xrc.XRCCTRL(self, 'm_bm_flash_tab')
        self.cb_flash_autoload = xrc.XRCCTRL(self, 'm_cb_flash_autoload')
        self.rx_flash_service = xrc.XRCCTRL(self, 'm_rx_flash_service')
        
        self.bm_flash_tab.Show(False)
        
        # bindings ----------------
        self.bm_flash_close.Bind(wx.EVT_LEFT_UP, self.CloseMe)
        #self.bm_flash_tab.Bind(wx.EVT_LEFT_UP, self.OnMakeTabClick)
        self.Bind(wx.EVT_CHECKBOX, self.SaveOptions, self.cb_flash_autoload)
        self.Bind(wx.EVT_RADIOBOX, self.SetService, self.rx_flash_service)
        
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)       
        self.st_flash_header.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
        self.st_flash_header.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        self.st_flash_header.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
        self.st_flash_header.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)
            
        #self.st_flash_using.SetLabel('Using: ' + self.parent.web_music_type)
        
        #self.bu_update_restart.Enable(False)    
        # set layout --------------
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(panel, 1, wx.EXPAND|wx.ALL, 5)
        self.SetSizer(sizer)
        self.SetAutoLayout(True)
        #self.LoadSetings()
        
        
        #*** if FLASH_ENABLED:
        try:
            self.parent.StopAll()
        except Exception, expt:
            print "Flash plug-in: " + str(Exception) + str(expt)
        
        #flash windows
        try:
            self.flash_window = player_flash.Player(self) #.mediaPlayer #FlashWindow(self.pa_flash_player, style=wx.NO_BORDER, size=wx.Size(500,140))#, size=(400, 120))
            self.parent.player = self.flash_window
            
            #self.flash.Show(True)
            
            flash_sizer = wx.BoxSizer(wx.VERTICAL)
            flash_sizer.Add(self.flash_window.mediaPlayer, 1, wx.EXPAND|wx.ALL, 5)
            self.pa_flash_player.SetSizer(flash_sizer)
                   
            self.parent.use_web_music = True
            self.parent.flash = self.flash_window
            self.parent.use_backend = 'flash'
        except Exception, expt:
            print "Flash plug-in: " + str(Exception) + str(expt)
            dlg = wx.MessageDialog(self, "Flash for Internet Explorer must be installed for this plug-in to work.", 'Alert', wx.OK | wx.ICON_WARNING)
            if (dlg.ShowModal() == wx.ID_OK):
                dlg.Destroy()
        ##self.parent.web_music_url = DIZZLER_URL
        ##self.parent.web_music_type = "Dizzler"
        ##self.MakeModal(False)
        
        self.LoadSettings()
        #self.SetService(None)
        
        #set a reciever to catch new song events
        self.parent.SetReceiver(self, 'main.playback.load')
        # ***else:
        # ***    dlg = wx.MessageDialog(self, "Flash for Internet Explorer must be installed for this plug-in to work.", 'Alert', wx.OK | wx.ICON_WARNING)
        # ***    if (dlg.ShowModal() == wx.ID_OK):
        # ***        dlg.Destroy()            
        
    def GenericReceiverAction(self, message):
        """Sets the pubsub receiver action."""
        self.GetService(None)

    def CloseMe(self, event=None):
        self.SaveOptions(None)
        self.parent.use_web_music = False
        self.parent.OnStopClick(None)
        self.parent.SetBackend(None)
        self.Destroy()
        
    def OnMakeTabClick(self, event=None):
        pass
    
    def OnMakeTabClick2(self, event=None):
        # transfer plug-in to tab in main player
        # make a new page                
        page1 = PageOne(self.parent.nb_main)
        # add the pages to the notebook
        self.parent.nb_main.AddPage(page1, "Flash")
        
        #flash windows
        flash_window = FlashWindow(page1, style=wx.NO_BORDER, size=wx.Size(500,140))#, size=(400, 120))        
        #self.flash.Show(True)        
        flash_sizer = wx.BoxSizer(wx.VERTICAL)
        flash_sizer.Add(flash_window, 1, wx.EXPAND|wx.ALL, 5)
        page1.SetSizer(flash_sizer)        
        self.parent.use_web_music = True
        #self.parent.flash = flash_window
        self.Destroy()
               
    #def LoadFlashSong(self, artist, song):
        #start playback
        #self.flash_window.movie = DIZZLER_URL + artist + "-" + song

    #def StopFlashSong(self):
        #stop playback
        #self.flash_window.movie = 'temp.swf' 
        
    #def SetDizzler(self, event):
        #stop playback
        #self.parent.web_music_url = DIZZLER_URL
        #self.parent.web_music_type = "Dizzler"
        #self.st_flash_using.SetLabel('Using Dizzler')
        
    #def SetGrooveShark(self, event):
        #stop playback
        #self.parent.web_music_url = DIZZLER_URL
        #self.parent.web_music_type = "GrooveShark"
        #self.st_flash_using.SetLabel('Using GrooveShark')
        
    def GetService(self, event):
        service = self.rx_flash_service.GetSelection()
        #print service
        if service == 0:
            #self.parent.web_music_url =''
            self.parent.current_song.song_url = GROOVESHARK_URL + str(self.parent.current_song.song_id)
            self.parent.web_music_type = "GrooveShark"
            print "GROOVESHARK"
        elif service == 1:
            #self.parent.web_music_url = DIZZLER_URL
            self.parent.current_song.song_url = DIZZLER_URL + self.parent.current_song.artist + "-" + self.parent.current_song.song
            self.parent.web_music_type = "Dizzler"
            print "DIZZLER"
        else:
            artist = self.parent.current_song.artist
            song = self.parent.current_song.song
            self.parent.current_song.song_url = jiwa.JiwaMusic().GetFlashUrlFirstResult(artist, song)
            self.parent.web_music_type = "Jiwa"
            print "JIWA"
            
    def SetService(self, event):
        self.SaveOptions(None)
        #MouseClicker(25, 220)
        
    def LoadSettings(self):
        #load the setting from settings_falsh.xml if it exists
        settings_dict = xml_utils().get_generic_settings(self.FLASH_SETTINGS + "settings_flash.xml")
        #print settings_dict
        if len(settings_dict) >= 1:
            autoload=0
            if settings_dict.has_key('autoload'):
                autoload = int(settings_dict['autoload'])
            self.cb_flash_autoload.SetValue(autoload)
            service=0
            if settings_dict.has_key('service'):
                service = int(settings_dict['service']) 
            self.rx_flash_service.SetSelection(service)
            if settings_dict.has_key('window_position'):
                # not good, replace eval
                self.SetPosition(eval(settings_dict['window_position']))
            if settings_dict.has_key('window_size'):
                self.SetSize(eval(settings_dict['window_size']))

    def SaveOptions(self, event):
        # save value to options.xml
        window_dict = {}        
        window_dict['autoload'] = str(int(self.cb_flash_autoload.GetValue()))
        window_dict['service'] = str(int(self.rx_flash_service.GetSelection()))
        window_dict['window_position'] = str(self.GetScreenPosition())
        window_dict['window_size'] = str(self.GetSize())#[0], self.GetSize()[1]))

        xml_utils().save_generic_settings(self.FLASH_SETTINGS, "settings_flash.xml", window_dict)

            
# --------------------------------------------------------- 
# titlebar-like move and drag
    
    def OnMouseLeftDown(self, evt):
        self.Refresh()
        self.ldPos = evt.GetEventObject().ClientToScreen(evt.GetPosition())
        self.wPos = self.ClientToScreen((0,0))
        self.CaptureMouse()

    def OnMouseMotion(self, evt):
        #print evt.GetPosition()
        #print self.GetScreenPosition() 
        
        if evt.Dragging() and evt.LeftIsDown():
            dPos = evt.GetEventObject().ClientToScreen(evt.GetPosition())
            #nPos = (self.wPos.x + (dPos.x - self.ldPos.x), -2)
            try:
                nPos = (self.wPos.x + (dPos.x - self.ldPos.x), self.wPos.y + (dPos.y - self.ldPos.y))
                self.Move(nPos)
            except Exception, expt:
                pass

    def OnMouseLeftUp(self, evt):
        try:
            self.ReleaseMouse()
        except wx._core.PyAssertionError:
            pass

    def OnRightUp(self, evt):
        #self.hide_me()
        #self..Destroy()
        pass
          
      
class PageOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)        
              
# ===================================================================            

              
charset = 'utf-8'
        
def url_quote(s, safe='/', want_unicode=False):
    """
    Wrapper around urllib.quote doing the encoding/decoding as usually wanted:
    
    @param s: the string to quote (can be str or unicode, if it is unicode,
              config.charset is used to encode it before calling urllib)
    @param safe: just passed through to urllib
    @param want_unicode: for the less usual case that you want to get back
                         unicode and not str, set this to True
                         Default is False.
    """
    if isinstance(s, unicode):
        s = s.encode(charset)
    elif not isinstance(s, str):
        s = str(s)
    #s = urllib.quote(s, safe)
    if want_unicode:
        s = s.decode(charset) # ascii would also work
    return s
     
# ===================================================================   

#import win32api
#import win32con
#win32api.keybd_event(win32con.VK_F3, 0) # this will press F3 key

#def MouseClicker(position_x, position_y):
 #   print position_x
 #   print win32api.GetFocus() # this will return you the handle of the window which has focus

  #  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, position_x, position_y, 0, 0) # this will press mouse left button
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 20, 20, 0, 0) # this will raise mouse left button
    #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 20, 20, 0, 0) # this will raise mouse left button
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, position_x, position_y) # this will press mouse left button
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, position_x, position_y) # this will press mouse left button
  #  print "clicky"

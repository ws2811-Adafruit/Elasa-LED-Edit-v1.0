__author__ = 'Hamed'
import Tkinter as tk
import PySide
#
# import Tkinter
# from Tkinter import Tk
# from Tkinter import Label
# def clickMe(): # 2
#     b.configure(text="** I have been Clicked! **")
#     # b.configure(text='Hello ' + name.get())
#     l.configure(foreground='red')
#
# root = Tkinter.Tk()
# l = Tkinter.Label(root, text="Hello, world!\nTkinter on PocketPC!\nSee http://pythonce.sf.net.")
# b = Tkinter.Button(root, text='Quit', command=clickMe)
# l.grid(column=1, row=0) # 3
# # Label(root, text="A Label").grid(column=0, row=0)
#
#
# l.pack()
# b.pack()
# root.title("Python GUI")
#
# # action = Tkinter.Button(root, text="Click Me!", command=clickMe) # 7
# # action.grid(column=1, row=0)
#
# # name = Tkinter.StringVar() # 6
# # nameEntered = Tkinter.Entry(root, width=12, textvariable=name) # 7
# # nameEntered.grid(column=0, row=1)
#
#
# root.mainloop()
#
#
#
# import Tkinter as tk
#
# class ExampleApp(tk.Frame):
#     ''' An example application for TkInter.  Instantiate
#         and call the run method to run. '''
#     def __init__(self, master):
#         # Initialize window using the parent's constructor
#         tk.Frame.__init__(self,
#                           master,
#                           width=300,
#                           height=200)
#         # Set the title
#         self.master.title('TkInter Example')
#
#         # This allows the size specification to take effect
#         self.pack_propagate(0)
#
#         # We'll use the flexible pack layout manager
#         self.pack()
#
#         # The greeting selector
#         # Use a StringVar to access the selector's value
#         self.greeting_var = tk.StringVar()
#         self.greeting = tk.OptionMenu(self,
#                                       self.greeting_var,
#                                       'hello',
#                                       'goodbye',
#                                       'heyo')
#         self.greeting_var.set('hello')
#
#         # The recipient text entry control and its StringVar
#         self.recipient_var = tk.StringVar()
#         self.recipient = tk.Entry(self,
#                                   textvariable=self.recipient_var)
#         self.recipient_var.set('world')
#
#         # The go button
#         self.go_button = tk.Button(self,
#                                    text='Go',
#                                    command=self.print_out)
#
#         # Put the controls on the form
#         self.go_button.pack(fill=tk.X, side=tk.BOTTOM)
#         self.greeting.pack(fill=tk.X, side=tk.TOP)
#         self.recipient.pack(fill=tk.X, side=tk.TOP)
#
#     def print_out(self):
#         ''' Print a greeting constructed
#             from the selections made by
#             the user. '''
#         print('%s, %s!' % (self.greeting_var.get().title(),
#                            self.recipient_var.get()))
#     def run(self):
#         ''' Run the app '''
#         self.mainloop()
#
# app = ExampleApp(tk.Tk())
# app.run()

import wx
import subprocess,os
inkscape_dir=r"C:\Program Files (x86)\SWFTools"
inkscape_dir=r"E:\soheil\web_site_root\ieee\all_functions\linux server\python GUI"
assert os.path.isdir(inkscape_dir)
os.chdir(inkscape_dir)
from PIL import Image
image_address='C:\Users\Hamed\Pictures\LED\led.jpg'
im = Image.open(image_address)
# xy=1;sss=im.getpixel(xy)
pixels = list(im.getdata())
pix = im.load()
print pix[0, 0]
# print 'PIXEL IS :'+ pixels[1,1]
width, height = im.size
# pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
# print 'test'+ pixels[1,1]

new_img = im.resize((220,220))
new_img.save('brick-house-256x256','png')


from PIL import Image
im = Image.open(image_address) #Can be many different formats.
pix = im.load()
print im.size #Get the width and hight of the image for iterating over
# print pix[x,y] #Get the RGBA Value of the a pixel of an image
# pix[x,y] = value # Set the RGBA Value of the image (tuple)

# swfextract -f 2 Double_angle_off.swf -o file.jpeg
# swfextract -j 447 Double_angle_off.swf -o file.jpeg



import subprocess,os
inkscape_dir=r"C:\Program Files (x86)\SWFTools"
inkscape_dir=r"E:\soheil\web_site_root\ieee\all_functions\linux server\python GUI"
assert os.path.isdir(inkscape_dir)
os.chdir(inkscape_dir)
# subprocess.Popen(['swfextract','-j','447','Double_angle_off.swf','-o','file.jpeg'])

import subprocess
st='"C:\Program Files (x86)\SWFTools\swfextract.exe" -j 447 Double_angle_off.swf -o file.jpg'
st='"C:\Program Files (x86)\SWFTools\swfrender.exe" -X 222 -Y 222 Double_angle_off.swf -o file.jpg'
# st='"C:\Program Files (x86)\SWFTools\swfextract.exe"  Double_angle_off.swf'

awk_sort = subprocess.Popen( [st ], stdin= subprocess.PIPE, stdout= subprocess.PIPE,shell=True)
awk_sort.wait()
output = awk_sort.communicate()[0]
print output.rstrip()
frontpage=output.rstrip()

ss=subprocess.call(st, shell=True)
# s1=ss.communicate()[0]

try:
        from subprocess import check_output
        import subprocess
        # ip = check_output(["dig", "+short", "@resolver1.opendns.com",
        #                    "myip.opendns.com"]).decode().strip()
        st='"C:\Program Files (x86)\SWFTools\swfextract.exe" -j 447 Double_angle_off.swf -o file.jpeg'

        output = subprocess.Popen([st], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        ip2 = output.communicate()[0]
        print
        ip2.rstrip()
        # internalIp = ip2.split('lo:')[1].replace(' ', '')
        # print internalIp
except:
        print 'We could not find internal ip of your app or your system,' \
        'problem maybe ocurred because this is working by linux system and you are using windows system'


from swf.movie import SWF
from swf.export import SVGExporter

# create a file object
file = open('C:/Users/Hamed/IGC/Desktop/trash/1.swf', 'rb')

# load and parse the SWF
swf = SWF(file)
# print SWF(file)
# create the SVG exporter
svg_exporter = SVGExporter()

# export!
svg = swf.export(svg_exporter)

# save the SVG
open('C:/Users/Hamed/IGC/Desktop/trash/1.svg', 'wb').write(svg.read())


#
# import gfx
#
# doc = gfx.open("swf", "C:/Users/Hamed/IGC/Desktop/trash/1.swf")
# for pagenr in range(1,doc.pages+1):
#     page = doc.getPage(pagenr)
#     print "Page", pagenr, "has dimensions", page.width, "x", page.height

from PIL import Image
i = Image.open(image_address)

pixels2 = i.load() # this is not a list, nor is it list()'able
width, height = i.size

all_pixels = []
for x in range(width):
    for y in range(height):
        cpixel = pixels2[x, y]
        all_pixels.append(cpixel)
from Tkinter import *
from PIL.ImageTk import PhotoImage
import os

def images_size(filepath):
    main= Tk()
    imgobj = PhotoImage(file=filepath)
    size=(imgobj.width(), imgobj.height())
    return size

def imageResize(filepath, size_index):
    from PIL import Image
    NEAREST=0
    file_dir=os.path.split(filepath)
    size=images_size(filepath)    # get image size
    new_size1=(int(size[0]*size_index), int(size[1]*size_index))  # set new size here
    new_size=(100,100)
    sourceimage = Image.open(filepath)
    sourceimage.resize(new_size, resample=NEAREST).save(file_dir[0]+'\\ico'+file_dir[1])
    print(file_dir[0]+'\\ico'+file_dir[1])


if __name__ == '__main__':
    imageResize('H:\ieee\\all_functions\linux server\python GUI\Grid_on_photo\input.png', size_index=0.5)
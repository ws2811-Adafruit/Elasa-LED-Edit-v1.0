from PIL import Image
from resizeimage import resizeimage

def resize_file(in_file, out_file, size):
    with open(in_file) as fd:
        image = resizeimage.resize_thumbnail(Image.open(fd), size)
    image.save(out_file)
    image.close()

resize_file('input.PNG', 'foo_small.jpg', (256, 256))
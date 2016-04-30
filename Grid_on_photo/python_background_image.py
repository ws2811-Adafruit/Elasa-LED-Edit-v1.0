import Image

background = Image.open("untitled2.jpg")
foreground = Image.open("input.png")

background.paste(foreground, (0, 0), foreground)
background.show()


background = Image.open("untitled2.jpg")
foreground = Image.open("input.png")

Image.alpha_composite(background, foreground).save("test3.png")
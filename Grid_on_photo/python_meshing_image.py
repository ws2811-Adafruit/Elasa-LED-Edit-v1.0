from PIL import Image, ImageDraw

MAP_BACKGROUND_FILE='input.png'
width=100;height=100
map_background = Image.open(MAP_BACKGROUND_FILE).convert('RGBA')
map_mesh = Image.new('RGBA', (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(map_mesh)

# Create mesh using: draw.line([...], fill=(255, 255, 255, 50), width=1)

map_background.paste(map_mesh, (0, 0), map_mesh)
map_background.paste((255,255,255), (0, 0), map_mesh)
map_background.save('ss.png')



import Image, ImageDraw, random
background = Image.new('RGB', (100, 100), (255, 255, 255))
MAP_BACKGROUND_FILE='icoinput.png'
width=100;height=100
foreground = Image.open(MAP_BACKGROUND_FILE).convert('RGBA')


# foreground = Image.new('RGB', (100, 100), (255, 0, 0))
mask = Image.new('L', (100, 100), 0)
# mask=Image.new('RGB', (100, 100), (255, 0, 0))
draw = ImageDraw.Draw(mask)
for i in range(0, 100, 2):
    draw.line((i, 0, i, 100),(256))
    draw.line((0, i, 100, i),(256))

    # draw.line((i, 0, i, 100), fill=random.randrange(256))
    # draw.line((0, i, 100, i), fill=random.randrange(256))
result = Image.composite(background, foreground, mask)
result.save('ss2.png')

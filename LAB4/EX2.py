from PIL import Image, ImageFont, ImageChops
from PIL import ImageDraw

scale = 2  # глобальное увеличение всего

width = int(400 * scale)
height = int(500 * scale)

image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)

center = (width / 2, width / 2)

shape = [(int(-35 * scale), int(-170 * scale)), (int(35 * scale), 0)]

overlay = Image.new('RGBA', (width, width))
edraw = ImageDraw.Draw(overlay)
edraw.ellipse([(x + center[0], y + center[0]) for x, y in shape], fill="#d164d1", outline="#cc35bf",
              width=int(width / 120))

n = 7  # количество лепестков
for i in range(n):
    angle = 360 * (i / n)
    rotated = overlay.rotate(angle, expand=False, center=center)
    image.paste(rotated, (0, 0), rotated)

shape = [(int(-40 * scale), int(-40 * scale)), (int(40 * scale), int(40 * scale))]
draw.ellipse([(x + center[0], y + center[0]) for x, y in shape], fill="#f2e230", outline="#edaf11",
             width=int(width / 120))

font = ImageFont.truetype("Britannic Bold Regular.ttf", size=int(scale * 100))

draw.text((int(width * 0.05), width - 30), "FLOWER", "#ee1234", font)

image.save("flower.png")  # сохранить на диск

new_image = Image.open("flower.png")  # открыть

noise = Image.effect_noise((width, height), 25)
rgbimg = Image.new("RGB", noise.size)
rgbimg.paste(noise)

# шум
new_image = ImageChops.overlay(image, rgbimg)

new_image.save("flower_noised.png")  # сохранить на диск

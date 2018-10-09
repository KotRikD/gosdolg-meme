from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps

from debtcalc import DebtCalc

font = ImageFont.truetype("font.ttf", 82)
color = (219,41,37)

sizes = (673, 79)
paddings = (173,248)

base_img = Image.open("mem.png").convert("RGB")

draw = ImageDraw.Draw(base_img)

def humanize(value):
    return "{:,}".format(round(value))

count = "$"+humanize(int(DebtCalc().debt))

w, h = draw.textsize(count, font=font)

draw.text(((sizes[0] - w) / 2 + paddings[0], (sizes[1] - h) / 2 + paddings[1]), count, fill=color, font=font, align="center")

base_img.save("test.jpeg", format="JPEG")
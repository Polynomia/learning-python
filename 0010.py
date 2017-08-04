#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import ImageFont, ImageDraw, ImageFilter, Image
import random, string


# 随机字母:
def rndChar():
    return random.choice(string.ascii_letters)


# 随机颜色1:
def rndColor():
    return (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def create_pic(filepath):
    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    for x in range(width):
        for y in range(width):
            draw.point((x, y), fill=rndColor())
    for t in range(4):
        draw.text((60 * t + 15, 10), rndChar(), font=myFont, fill=rndColor2())
    img = img.filter(ImageFilter.BLUR)
    img.save(filepath, 'jpeg')


if __name__ == '__main__':
    myFont = ImageFont.truetype('source/0000/msyh.ttf', size=36)
    width = 60 * 4
    height = 60
    create_pic('source/0010.jpg')

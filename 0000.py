#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果
from PIL import Image, ImageFont, ImageDraw


def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('source/0000/111.ttf', size=40)
    color = '#ff0000'
    width, height = img.size
    draw.text((width - 90, 5), u'地方', font=myfont, fill=color)
    img.save('source/0000/result.jpg', 'jpeg')


if __name__ == '__main__':
    image = Image.open('source/0000/1.png')
    add_num(image)

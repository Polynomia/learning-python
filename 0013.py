#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)[http://tieba.baidu.com/p/2166231880]
import os
from  bs4 import BeautifulSoup
from urllib.request import urlopen


def get_pic(init_url):
    html = urlopen(init_url)
    bs = BeautifulSoup(html, 'lxml')
    pic_urls = bs.findAll('img', {"bdwater": "杉本有美吧,1280,860"})
    for pic_url in pic_urls:
        down_pic(pic_url['src'])


def down_pic(src_url):
    content = urlopen(src_url).read()
    with open('source/0013/' + os.path.basename(src_url), 'wb') as f:
        f.write(content)
    print('download %s' % (os.path.basename(src_url)))


if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/2166231880'
    get_pic(url)

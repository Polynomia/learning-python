#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#第 0009 题： 一个HTML文件，找出里面的链接。

import os,re,codecs

def get_link(filepath,savepath):
    if os.path.isfile(filepath) and os.path.splitext(filepath)[1] == '.html':
        print('open')
        reTxt = re.compile(r'"((http|https|ftp|ftps)://.*?)"')
        with codecs.open(filepath, 'r', 'utf8') as f:
            data = f.read()
            links = reTxt.findall(data)
            assert os.path.isfile(savepath)
            with codecs.open(savepath, 'w', 'utf8') as s:
                for link in links:
                    print(link[0],file=s)
            s.close()
        f.close()
    return

if __name__ =='__main__':
    get_link('source/0009/test.html','source/0009/output.txt')
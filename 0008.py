#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#第 0008 题： 一个HTML文件，找出里面的正文

import os,re,codecs

def get_body(filepath,savepath):
    if os.path.isfile(filepath) and os.path.splitext(filepath)[1]=='.html':
        reTxt=re.compile(r'<body>[\s\S]*</body>')
        with codecs.open(filepath,'r','utf8') as f:
            data = f.read()
            body = reTxt.findall(data)
            with codecs.open(savepath,'w','utf8') as s:
                print(''.join(body), file= s)
            s.close()
        f.close()
    return

if __name__ == '__main__':
    get_body('source/0008/test.html','source/0008/output.txt')
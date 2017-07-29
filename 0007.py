#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os, re, codecs


def count_code(dir_path):
    if not os.path.isdir(dir_path):
        print('NOT A PATH')
        return
    comment_re = re.compile(r'(\s*)#')
    filelist = os.listdir(dir_path)
    for file in filelist:
        filepath = os.path.join(dir_path, file)
        if os.path.isfile(filepath) and os.path.splitext(filepath)[1] == '.py':
            f = codecs.open(filepath, 'r', 'utf-8')
            all = 0
            comment = 0
            space = 0
            for line in f.readlines():
                all += 1
                if line.strip() == '':
                    space += 1
                    continue
                if comment_re.match(line):
                    comment += 1
            print('%s: %s lines, %s comments, %s space lines' % (file, all, comment, space))
            f.close()


if __name__ == '__main__':
    count_code('source/0007')

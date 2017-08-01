#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
[
	[1, 82, 65535],
	[20, 90, 13],
	[26, 809, 1024]
]
"""
import json, codecs, xlwt


def main():
    with codecs.open('source/0016/numbers.txt', 'r', 'utf8') as f:
        data = json.load(f)
        workbook = xlwt.Workbook()
        num_sheet = workbook.add_sheet('numbers')
        for index, datas in enumerate(data):
            for index2, num in enumerate(datas):
                num_sheet.write(index, index2, num)
        workbook.save('source/0016/numbers.xls')


if __name__ == '__main__':
    main()

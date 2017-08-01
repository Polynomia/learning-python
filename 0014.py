#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中，如下图所示：
"""
import json, xlwt, codecs
from collections import OrderedDict


def main():
    with codecs.open('source/0014/student.txt', 'r', 'utf8') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)
        workbook = xlwt.Workbook()
        stu_sheet = workbook.add_sheet('student', cell_overwrite_ok=True)
        for index, (key, values) in enumerate(data.items()):
            stu_sheet.write(index, 0, key)
            for i, value in enumerate(values):
                stu_sheet.write(index, i + 1, value)
        workbook.save('source/0014/student.xls')


if __name__ == '__main__':
    main()

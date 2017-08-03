#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如
下所示：
<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!--
    学生信息表
    "id" : [名字, 数学, 语文, 英文]
-->
{
    "1" : ["张三", 150, 120, 100],
    "2" : ["李四", 90, 99, 95],
    "3" : ["王五", 60, 66, 68]
}
</students>
</root>
"""
import xlrd, json
from lxml import etree


def read_exl(filepath):
    exl = xlrd.open_workbook(filepath)
    exl_sheet = exl.sheet_by_name('student')
    data = dict()
    for i in range(exl_sheet.nrows):
        data[exl_sheet.row_values(i)[0]] = exl_sheet.row_values(i)[1:]
    print(json.dumps(data, ensure_ascii=False))
    return json.dumps(data, ensure_ascii=False)


def convert2xml(data, filename):
    root = etree.Element('root')
    students = etree.SubElement(root, 'students')
    students.append(etree.Comment(u'""学生信息表 "id" : [名字, 数学, 语文, 英文]""'))
    students.text = data
    student_xml = etree.ElementTree(root)
    student_xml.write(filename, pretty_print=True, xml_declaration=True, encoding='utf-8')


if __name__ == '__main__':
    content = read_exl('source/0014/student.xls')
    convert2xml(content, 'source/0014/student.xml')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0020 题：
登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，
然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，
就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。
写代码，对每月通话时间做个统计。
"""
import xlrd


def count_time(filepath):
    exl = xlrd.open_workbook(filepath)
    sheet = exl.sheet_by_index(0)
    row_num = sheet.nrows
    total = 0
    for i in range(1, row_num):
        total += int(sheet.cell_value(i, 3))
    year = int(sheet.cell_value(1, 1)[0:4])
    month = int(sheet.cell_value(1, 1)[5:7])
    seconds = total % 60
    minutes = (total % (60 * 60)) // 60
    hours = total // (60 * 60)
    print("在%d年%d月您的通话时长为：%d小时%d分钟%d秒" % (year, month, hours, minutes, seconds))


if __name__ == '__main__':
    count_time('source/0020/src.xls')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 任一个英文的纯文本文件，统计其中的单词出现的个数
import re, codecs

fin = codecs.open('source/0006/diary1.txt', 'r', 'utf-8')
str = fin.read()
reTxt = re.compile('(\w+)')
words = reTxt.findall(str)

wordDict = dict()


def f(word):
    if word.lower() in wordDict:
        wordDict[word.lower()] += 1
    else:
        wordDict[word.lower()] = 1


for word in words:
    f(word)

for key, value in wordDict.items():
    print('%s,%d' % (key, value))

fin.close()

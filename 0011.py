#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第 0011 题： 敏感词文本文件 filtered_words.txt，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

import codecs


def get_words(filepath, word_list):
    with codecs.open(filepath, 'r', 'utf8') as f:
        for w in f.readlines():
            word_list.append(w.strip())


if __name__ == '__main__':
    path = 'source/0011/filtered_words.txt'
    word_list = []
    get_words(path, word_list)
    print(word_list)

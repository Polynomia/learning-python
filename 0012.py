#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，
# 例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
# 如果是英文我只用一个*代替
import codecs, re


def get_words(filepath, word_list):
    with codecs.open(filepath, 'r', 'utf8') as f:
        for w in f.readlines():
            word_list.append(w.strip())


def get_dic(word_list):
    dic = dict()
    for word in word_list:
        if len(re.findall(u"[\u4e00-\u9fa5]+", word)) > 0:
            dic[word] = len(word) * '*'
        else:
            dic[word] = '*'
    return dic


def main():
    path = 'source/filtered_words.txt'
    word_list = []
    get_words(path, word_list)
    dic = get_dic(word_list)
    while True:
        print('pls input your words(input exit for exiting):')
        words = input()
        if words == 'exit':
            break
        for word in word_list:
            reTxt = re.compile(r'' + word + '')
            words = reTxt.sub(dic[word], words)
        print(words)


if __name__ == '__main__':
    main()

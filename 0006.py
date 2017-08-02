# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词
import os, re, codecs


def find_word(path):
    reTxt = re.compile('(\w+)')
    if not os.path.isdir(path):
        print('NOT A PATH')
        return
    filelist = os.listdir(path)
    for file in filelist:
        filepath = os.path.join(path, file)
        if os.path.isfile(filepath) and os.path.splitext(filepath)[1] == '.txt':
            f = codecs.open(filepath, 'r', 'utf-8')
            data = f.read()
            words = reTxt.findall(data)
            wordDict = dict()
            for word in words:
                word = word.lower()
                if word in wordDict:
                    wordDict[word] += 1
                else:
                    wordDict[word] = 1
            ansList = sorted(wordDict.items(), key=lambda t: t[1], reverse=True)
            print('file: %s->the most word: %s' % (file, ansList[0][0]))
            f.close()


if __name__ == '__main__':
    find_word('source/0006')

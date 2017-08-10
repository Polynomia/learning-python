#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from termcolor import *
import re, sys

url = 'http://dict.youdao.com/w/eng/'


class word_search():
    def __init__(self, word):
        self.word = word
        self.bs = self.get_bs()
        self.typo = self.get_typoDef()
        if not self.typo:
            self.definition = self.get_definitions()
            self.soundmark = self.get_soundmark()
            self.examples = self.get_examples()
        else:
            self.definition = None
            self.soundmark = None
            self.examples = None

    def get_bs(self):
        try:
            html = urlopen(url + self.word)
            bsObj = BeautifulSoup(html.read(), 'lxml')
            return bsObj
        except HTTPError or URLError as e:
            if hasattr(e, 'reason'):
                print(e.reason)
            return None

    def get_typoDef(self):
        content = self.bs.find("div", {"class": "error-typo"})
        if not content:
            return None
        new_word = content.find("a", {"class": "search-js"}).get_text()
        reDef = re.compile('</span>[\s]*\n*(.*?)[\s]*\n*</p>')
        typo_def = reDef.search(str(content)).group(1)
        return new_word, typo_def

    def get_definitions(self):
        dic = self.bs.find("div", {"class": "trans-container"}).find_all("li")
        definition = []
        for defi in dic:
            definition.append(defi.get_text())
        return definition

    def get_examples(self):
        examples = self.bs.find("div", {"id": "bilingual"}).find_all("p")
        sentence = []
        for ex in examples:
            sentence.append(ex.get_text().strip())
        engSentence = sentence[::3]
        chSentence = sentence[1::3]
        return zip(engSentence, chSentence)

    def get_soundmark(self):
        phonetic = self.bs.find("div", {"class": "baav"})
        sound = [pro.get_text() for pro in phonetic.find_all("span", {"class": "phonetic"})]
        return sound

    def show(self):
        print(colored(self.word, "white", attrs=['bold']), end=' ')
        if not self.typo:
            for x in self.soundmark:
                print(colored(x, "blue"), end=" ")
            print('')
            for x in self.definition:
                print(colored(x, "cyan"))
            for (x, y) in self.examples:
                print(colored(x, "white"))
                print(colored(y, "yellow"))
        else:
            print("\n您要找的是不是：%s" % (self.typo[0]))
            print(self.typo[1])


if __name__ == '__main__':
    word = ' '.join(sys.argv[1:])
    search = word_search(word)
    search.show()

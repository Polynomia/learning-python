#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
import re

url = 'http://dict.youdao.com/w/eng/'


def get_bs(word):
    try:
        html = urlopen(url + word)
        bsObj = BeautifulSoup(html.read(), 'lxml')
        return bsObj
    except HTTPError or URLError as e:
        if hasattr(e, 'reason'):
            print(e.reason)
        return None


def get_typoDef(bsObj):
    content = bsObj.find("div", {"class": "error-typo"})
    if not content:
        return None
    new_word = content.find("a", {"class": "search-js"}).get_text()
    reDef = re.compile('</span>[\s]*\n*(.*?)[\s]*\n*</p>')
    typo_def = reDef.search(str(content)).group(1)
    return new_word, typo_def


def get_definitions(bsObj):
    dic = bsObj.find("div", {"class": "trans-container"}).find_all("li")
    definition = []
    for defi in dic:
        definition.append(defi.get_text())
    print(definition)
    return definition


def get_examples(bsObj):
    examples = bs.find("div", {"id": "bilingual"}).find_all("p")
    sentence = []
    for ex in examples:
        sentence.append(ex.get_text().strip())
    engSentence = sentence[::3]
    chSentence = sentence[1::3]
    return (engSentence, chSentence)


def get_soundmark(bsObj):
    phonetic = bsObj.find("div",{"class":"baav"})
    sound = [pro.get_text() for pro in phonetic.find_all("span",{"class":"phonetic"})]
    return sound


if __name__ == '__main__':
    word = 'polynomial'
    bs = get_bs(word)
    if not get_typoDef(bs):
        definitions = get_definitions(bs)
        eng, ch = get_examples(bs)
        print(eng, ch)
        get_soundmark(bs)
        print(get_soundmark(bs))
    else:
        print(get_typoDef(bs))

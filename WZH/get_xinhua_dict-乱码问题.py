# coding=utf8

import requests
from bs4 import BeautifulSoup
import re

import sys
import codecs
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/57.0.2987.110 Safari/537.36','referer':"www.mmjpg.com"}


list_yin = list('āáǎàōóǒòēéěèīíǐìūúǔùǖǘǚǜ')
list_yin_replace = list('aaaaooooeeeeiiiiuuuuvvvv')
dict_yin_replace = dict(zip(list_yin, list_yin_replace))


dict_yin = {}
for i, yin in enumerate(list_yin):
    dict_yin[yin] = (i % 4) + 1

def pinyin_replace_func(pinyin):
    for key, value in dict_yin_replace.items():
        pinyin = pinyin.replace(key, value)
    return pinyin

# dict_has = {}
# with open('../hz_tone.txt', encoding ='utf-16') as f:
#     for line in f:
#         word_pinyin, num, str_yin, *other = line.strip().split()
#         fw.write(line.strip() + '\n')
#         dict_has[word_pinyin] = 1


for i in range(1, 2):
    url='http://xh.5156edu.com/html3/{0}.html'.format(str(i))
    print (url)
    html = requests.get(url, headers=headers)
    # print (html)
    html.encoding = 'gb18030'
    soup = BeautifulSoup(html.text, 'lxml')
    try:
        print (soup)
        a = soup.find('td', class_='font_22', align_ = 'center')
        print (a)
        # print (a.text)
    except Exception as e:
        print ('error', str(e))
        continue










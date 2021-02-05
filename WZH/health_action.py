# -*- coding: utf-8 -*-
################################################################################
#
# All Rights Reserved
#
################################################################################
"""
微博热搜爬虫

Authors: zhaowenfeng(zhaowenfeng@baidu.com)
Date:    2020/02/13
"""
import datetime
from copy import deepcopy
import sys
reload(sys)

sys.setdefaultencoding('utf-8')

import time
import random
import requests
# import MySQLdb
from bs4 import BeautifulSoup


def fetch_url(url):
    """
    抓取数据
    :param url:
    :return:
    """
    _headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "text/html; charset=utf-8",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/57.0.2987.133 Safari/537.36"
    }
    r = None
    try_time = 3
    try_sucess = False
    # 重试机制，增加链接成功的可能性
    while not try_sucess and try_time > 0:
        try:
            r = requests.get(url, headers=_headers, timeout=10)
            try_sucess = True
        except:
            time.sleep(random.randint(0, 5))
            try_time -= 1
            try_sucess = False
            continue
    if r is not None:
        return BeautifulSoup(r.content, features='lxml')
    else:
        return None

def process_spider():
    """
    实际爬虫过程
    :return:
    """
    fout = open('./result', 'w+')
    for i in range(1, 80):
        # 本地保留一份数据
        # file = open("./data/weibo_hot" + str(self.event_day) + "." + str(self.event_hour) + ".txt", "w+")
        # mysql_list = []
        # 获取url原始数据

        url = 'https://www.hiyd.com/dongzuo/?page=' + str(i)
        soup = fetch_url(url)
        data = soup.find('div', {'class': 'o-pagemod-bd'}).find('div', {'class': 'o-exercise-list'})
        # 拉取每一个热搜榜数据
        for tr in data.find_all('li', {'class': 'hvr-glow'}):
            dd = tr.find('div', {'class': 'avatar-pic'}).find('img')
            x = str(dd).split('\"')
            word = x[1].strip().split()[0]
            fout.write(word + '\n')

process_spider()



# -*- coding: utf-8 -*-
################################################################################
#
# All Rights Reserved
#
################################################################################
"""
微博热搜爬虫

"""
import datetime
from copy import deepcopy
import sys
# reload(sys)
#
# sys.setdefaultencoding('utf-8')

import time
import random
import requests
# import MySQLdb
from bs4 import BeautifulSoup

from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
#引入ActionChains鼠标操作类
from selenium.webdriver.common.action_chains import ActionChains

driver= webdriver.Chrome('/Library/Frameworks/Python.framework/Versions/3.6/chromedriver')
driver.set_page_load_timeout(30)


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
    fout = open('./result_2', 'w+')
    soup =  fetch_url('https://www.gotokeep.com/training')
    ha = soup.find('div', {'class': 'keep-wrapper training'})
    # print (a)
    
    ul = ha.find('ul', {'class': 'workout-hashtag clearfix'})
    # print (ul)
    for li in ul.find_all('li'):
        xss = li.find('a').find('div', {'class': 'title'})
        fout.write(xss.text + '\n')

process_spider()






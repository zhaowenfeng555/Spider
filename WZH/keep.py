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
    fout = open('./result', 'w+')
    soup =  fetch_url('https://www.gotokeep.com/training')
    ha = soup.find('div', {'class': 'keep-wrapper point'})
    # print (a)
    
    ul = ha.find('ul', {'class': 'training-point clearfix'})
    # print (ul)
    for li in ul.find_all('li'):
        xss = li.find('a')
        hr = xss['href']
        url = 'https://www.gotokeep.com' + str(hr)

        driver.get(url)

        # 加载到底部
        all_window_height = []
        all_window_height.append(driver.execute_script("return document.body.scrollHeight;"))
        while True:
            driver.execute_script("scroll(0,100000)")  # 执行拖动滚动条操作
            time.sleep(3)
            check_height = driver.execute_script("return document.body.scrollHeight;")
            if check_height == all_window_height[-1]:
                break
            else:
                all_window_height.append(check_height)  # 如果不想等，将当前页面最大高度加入列表。

        data = driver.find_element_by_class_name('keep-wrapper')
        print(len(data.find_elements_by_class_name('name')))
        for tr in data.find_elements_by_class_name('name'):
            print(tr.text)
            fout.write(tr.text + '\n')

process_spider()






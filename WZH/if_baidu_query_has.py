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
    fout = open('./result_top5_number.txt', 'w+')

    with open('./result_all_word_info_query.txt_half') as f:
        for line in f:
            # lmx	李明鑫(sougou_xunfei) 刘明星(sougou_xunfei) 李美霞(sougou_xunfei)
            # dadaxingqiu     xuefei_ios      大大星球(da|da|xing|qiu)        有      无      一有一无
            pinyin, flag, word_pinyin, f1, f2, f3 = line.strip().split('\t')
            for w_f in str_wd.strip().split():
                wd = w_f.split('(')[0]
                wf = w_f.split('(')[1].strip(')')
                # 本地保留一份数据
                # file = open("./data/weibo_hot" + str(self.event_day) + "." + str(self.event_hour) + ".txt", "w+")
                # mysql_list = []
                # 获取url原始数据
                try:

                    url = """https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd={0}&oq=%25E4%25BB%2580%25E4%25B9%2588&rsv_pq=d217527400053fdb&rsv_t=08bfMRgJY3ClPzB9RHP69seNWoYK%2BmUyYliu2fm1bCP3t5mZ%2BdZWS1Moj5A&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=17&rsv_sug1=15&rsv_sug7=101&rsv_sug2=0&rsv_btype=t&inputT=4079&rsv_sug4=4965""".format(wd)
                    soup = fetch_url(url)
                    flag = 0
                    i = 0
                    xx = soup.find('div', {'id': 'content_left'}).find_all('div')
                    for tr in xx:
                        i += 1
                        if i >= 6:
                            break
                        #print (wd + ' ' + str(tr))
                        try:
                            dd = tr.find('h3').find('a')
                        except:
                            i -= 1
                            continue
                            #i -= 1
                        #print (wd + ' ' + str(i) + ' ' + str(dd))

                        #print (dd)
                        #print (wd)
                        #print (unicode(dd).find(unicode(wd)) >= 0)
                        if unicode(dd).find(unicode(wd)) >= 0:
                            flag += 1
                                #break
                    fout.write('\t'.join([pinyin, wf, wd, str(flag)]) + '\n')
                except:
                    continue
            #if pinyin == 'bukejigou':
             #   sys.exit(1)

process_spider()



#! -*- coding:utf-8 -*-
import datetime
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver

# 把find_elements 改为　find_element
def getUrl():

    one_url = 'https://fanyi.baidu.com/translate?aldtype=16047&query=+#jp/zh/'

    jiaming_W = 'ない'

    f_url = one_url+ jiaming_W


    html = get_one_page(f_url)
    print(html)



    # big_list = []
    # selector = etree.HTML(html)
    # meaning = selector.xpath('//*[@id="main-outer"]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/p[2]/span/text()')
    # print(html)

def get_one_page(url):
    req = requests.get(url)
    #  requests 中文编码的终极办法！
    if req.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(req.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = req.apparent_encoding

        # encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
        global encode_content
        encode_content = req.content.decode(encoding, 'replace')  # 如果设置为replace，则会用?取代非法字符；
        return (encode_content)



getUrl()
        # 存储到MySQL中

def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='JOB',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany('insert into xian_python_link (jobs,link,firms) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration:
        pass









#-*- coding:utf-8 -*-
import datetime
import time

import pymysql
import requests
import re
from lxml import etree


from j_links import f_l



def get_one_page(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre'
    }
    response = requests.get(url)
    html =response.text
    return html
#

def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it[:12].split())
        new_items.append(f)
    return new_items


# sentense_re =

#  先组成一个大字符串，再用逗号分隔成若干个完整句子

def cut_plus_str(items):
    f_list = []
    item1 = "".join(items).split("。")
    for it in item1:

        f_items = "".join(it).strip()
        f_list.append(f_items)
    return f_list[:-1]

# title_xpa,extenses_xpa,meaning_xpa

def parse_one_page(html):
    big_list =[]
    article_re = '<article id="(.*?)".*?</article>'
    try:

        patt = re.compile(article_re,re.S)
        art_ite  = re.findall(patt,html)
        title_xpa = '//*[@id="%s"]/header/h1/text()' % art_ite[0]
        extenses_xpa = '//*[@id="%s"]/div/p/text()' % art_ite[0]
        meaning_xpa = '//*[@id="%s"]/div/p[last()]/text()' % art_ite[0]
        selector = etree.HTML(html)
        title = selector.xpath(title_xpa)
        extenses = selector.xpath(extenses_xpa)
        meaning = selector.xpath(meaning_xpa)
        c_setenses= cut_plus_str(extenses)
        l_num = len(c_setenses)
        f_title = title * l_num
        f_meaning = meaning * l_num
        for i1,i2,i3 in zip(f_title,f_meaning,c_setenses):
            big_list.append((i1,i3,i2))
    except:
        pass
    return big_list


def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JP',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into J_sentense (title_xpa,extenses_xpa,meaning_xpa) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass

if __name__ == "__main__":
    for url in f_l:

        html = get_one_page(url)
        content =parse_one_page(html)
        insertDB(content)
        print(datetime.datetime.now())
        time.sleep(1)
    print("下载完成")

# title_xpa,extenses_xpa,meaning_xpa


# create table J_sentense(
# id int not null primary key auto_increment,
# title_xpa text ,
# extenses_xpa text ,
# ls text
# ) engine=InnoDB  charset=utf8;
#
# drop table J_sentense;





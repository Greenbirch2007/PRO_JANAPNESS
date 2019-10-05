#-*- coding:utf-8 -*-
import time

import pymysql
import requests
import re
from lxml import etree


from s_link import url_l




def get_one_page(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre'
    }
    response = requests.get(url,headers=headers)
    html =response.text
    return html
#

def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it[:12].split())
        new_items.append(f)
    return new_items



#解析pdf文件的下载地址
def parse_one_page(html):
    big_list =[]
    selector=etree.HTML(html)
    titles = selector.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/h3/text()')
    for item in titles:
        big_list.append(item)

    patt = re.compile('^链接href="(.*?)" target="_blank"$',re.S)
    items = re.findall(patt,html)
    return items
    # for item in items:
    #     big_list.append(item)
    # return big_list


# def insertDB(content):
#     connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
#                                  db='JP',
#                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
#     cursor = connection.cursor()
#     try:
#         cursor.executemany('insert into Dijing_riyu (title,link,code) values (%s,%s,%s)', content)
#         connection.commit()
#         connection.close()
#         print('向MySQL中添加数据成功！')
#     except StopIteration:
#         pass


if __name__ == "__main__":
    for url in url_l:


        html = get_one_page(url)
        content = parse_one_page(html)
        # insertDB(content)

        print(content)
        time.sleep(2)



# title,link,code
# create table Dijing_riyu(
# id int not null primary key auto_increment,
# title varchar(20),
# link varchar(50),
# code varchar(10),
# LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
# ) engine=InnoDB  charset=utf8;
#
'>链接.*?^href="(.*?)" target="_blank"4' \






'' \
'' \
'' \
'' \
' style="font-size: 14px; text-decoration: underline;"><span style="font-size: 14px;">https://pan.baidu.com/s/1gJvQem8ES3YIj_NPqDO0Qg</span></a><span style="font-size: 14px;"> 提取码: 1ta2&nbsp;</span></p>'

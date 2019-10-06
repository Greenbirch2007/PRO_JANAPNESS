#! -*- coding:utf-8 -*-
import re
import time

import pymysql
from selenium import webdriver
from lxml import etree



from word_coll import w_l



def get_one_page(url):



    driver.get(url)
    html = driver.page_source
    return html



def parse_html(html):
    big_list =[]
    selector=etree.HTML(html)
    try:


        keyword = selector.xpath('//*[@id="jcTrans"]/h2/span/text()')
        patt = re.compile('<p class="sense-title">(.*?)</p>',re.S)
        items = re.findall(patt,html)
        new_item = "".join(items)
        big_list.append((keyword[0],new_item))
        return big_list
    except IndexError:
        pass





        # 存储到MySQL中

def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                 db='JP',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany('insert into Youdao_trans (keyword,meaning) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except StopIteration:
        pass








if __name__ == '__main__':
    for jiaming_W in w_l:
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)

        one_url = 'http://www.youdao.com/w/jap/'+ jiaming_W+'/#keyfrom=dict2.index'

        f_url = one_url+ jiaming_W


        html = get_one_page(f_url)
        time.sleep(1)

        content = parse_html(html)
        driver.quit()

        time.sleep(1)
        insertDB(content)
        print(content)



#
# create table Youdao_trans(
# id int not null primary key auto_increment,
# keyword varchar(20),
# meaning varchar(150),
# LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
# ) engine=InnoDB  charset=utf8;


# drop  table Youdao_trans;
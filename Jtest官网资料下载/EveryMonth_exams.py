#-*- coding:utf-8 -*-

import requests
import re
from lxml import etree






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



#解析pdf文件的下载地址
def parse_one_page(html):
    selector=etree.HTML(html)
    titles = selector.xpath('//*[@id="post-2066"]/p/a/text()')
    f_titles = remove_block(titles)
    links= selector.xpath('//*[@id="post-2066"]/p/a/@href')
    for i1,i2 in zip(f_titles,links):

        response = requests.get(i2)
        print(response.status_code)
        if response.status_code == 200:
            with open("/home/w/ForJtest/%s" % i1) as f:  # 切片之后优化了命名
                f.write(response.content)
                f.close()
        else:
            pass



if __name__ == "__main__":
    url = 'http://j-test.jp/page_id2066'

    html = get_one_page(url)
    parse_one_page(html)

    print("下载完成")










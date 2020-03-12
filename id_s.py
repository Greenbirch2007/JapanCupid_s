

import datetime
import re
import pymysql
import requests
from lxml import etree
import json
from queue import Queue
import threading
from requests.exceptions import RequestException











def parse_html(html):
    patt = re.compile('<a id="(.*?)" class="absolute top-minus-100"></a>',re.S)
    items = re.findall(patt,html)
    print(items)

# loop = asyncio.get_event_loop()
# fun_list = (get_title(i) for i in range(1,31))
# loop.run_until_complete(asyncio.gather(*fun_list))









# -*- coding:utf-8 -*-
import datetime
import re
import time

import pymysql

from lxml import etree
from selenium import webdriver




def get_first_page(url):

    driver.get(url)
    html = driver.page_source
    return html



# 可以尝试第二种解析方式，更加容易做计算
def parse_stock_note(html):

    selector = etree.HTML(html)
    code = selector.xpath('//*[@id="pro_body"]/center/div[5]/h1/strong/text()')
    profits= selector.xpath('//*[@id="right_col"]/table/tbody/tr[1]/td/table/tbody/tr[7]/td/text()')
    d_2018= "".join(profits[1][:-3].split(","))
    d_2017= "".join(profits[2][:-3].split(","))
    d_2016= "".join(profits[3][:-3].split(","))

    big_tuple = (code[0],d_2018,d_2017,d_2016)
    return big_tuple






def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into js_FinData (name,d2018,d2017,d2016,industry) values (%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass

#
if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)
    url = 'https://www.japancupid.com/en/results/matches?pageno=3'
    html = get_first_page(url)
    content = parse_html(html)
    print(content)




# 因为板块数据是最后嵌套进去的，所以要保持，１．数据库表结构，２．解析整理后的数据结构　３．　插入的字段结构　三者之间都要保持一致
# create table js_FinData(
# id int not null primary key auto_increment,
# name varchar(50),
# d2018 varchar(20),
# d2017 varchar(20),
# d2016 varchar(20),
# industry varchar(8)
# ) engine=InnoDB  charset=utf8;

#  drop table js_FinData;

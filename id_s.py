

import datetime
import re
import pymysql
import requests
from lxml import etree
import json
from queue import Queue
import threading
from requests.exceptions import RequestException






import asyncio
import aiohttp


def run_forever(func):
    def wrapper(obj):
        while True:
            func(obj)
    return wrapper







# async def get_title(i):

#     url = 'https://www.japancupid.com/en/results/matches?pageno={0}'



#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as resp:
#             print(resp.status)
#             text = await resp.text()
#             print('start', i)

#     big_list = []
#     al_id = re.compile('<a id="(.*?)" class="absolute top-minus-100"></a>',re.S)
#     items = re.findall(text,al_id)
#     for item in items:
#         big_list.append(item)
#     print(items)
#     time.sleep(8)
    





    # connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Yahoo_J',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    # cursor = connection.cursor()
    # try:
    #     cursor.executemany('insert into Tokyo_CFA (salary,type,link,job_name) values (%s,%s,%s,%s)', big_list)
    #     connection.commit()
    #     connection.close()
    #     print('向MySQL中添加数据成功！')
    # except TypeError :
    #     pass




def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_html(html):
    patt = re.compile('<a id="(.*?)" class="absolute top-minus-100"></a>',re.S)
    items = re.findall(patt,html)
    print(items)

# loop = asyncio.get_event_loop()
# fun_list = (get_title(i) for i in range(1,31))
# loop.run_until_complete(asyncio.gather(*fun_list))

url = 'https://www.japancupid.com/en/results/matches?pageno=3'


html = call_page(url)
print(html)
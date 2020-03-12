
#! -*- coding:utf-8 -*-
import datetime
import urllib


import os

from id_s import l_id
# 通过算法优势把图片给弄下来
#关键是找到id





import asyncio
import aiohttp


def run_forever(func):
    def wrapper(obj):
        while True:
            func(obj)
    return wrapper






async def get_title(i1,i2):


    url__p = 'https://cdn.japancupid.com/memphoto/Photo{0}/big/{1}.jpg'.format(i1,i2)



    async with aiohttp.ClientSession() as session:
        async with session.get(url__p) as resp:
            try:

                ln = os.getcwd()
                await urllib.request.urlretrieve(url__p, '{0}/{1}.jpg'.format(ln, url__p[-11:-4] + url__p[-22:-16]))
            except:
                pass




if __name__ == "__main__":
    print(datetime.datetime.now())
    s = datetime.datetime.now()


    loop = asyncio.get_event_loop()
    fun_list = (get_title(i1,i2) for i1 in range(1,4) for i2 in l_id)
    loop.run_until_complete(asyncio.gather(*fun_list))
    print(datetime.datetime.now())
    e = datetime.datetime.now()
    all_t = e-s








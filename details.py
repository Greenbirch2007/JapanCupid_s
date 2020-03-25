
#! -*- coding:utf-8 -*-
import datetime
import urllib.request


import os

from id_s import l_id
# 通过算法优势把图片给弄下来
#关键是找到id










def get_title(i1,i2):


    url__p = 'https://cdn.japancupid.com/memphoto/Photo{0}/big/{1}.jpg'.format(i1,i2)


    ln = os.getcwd()
    urllib.request.urlretrieve(url__p, '{0}/{1}.jpg'.format(ln, url__p[-11:-4] + url__p[-22:-16]))





if __name__ == "__main__":
    print(datetime.datetime.now())
    s = datetime.datetime.now()
    for i1 in range(1,5):
        for i2 in l_id:
            get_title(i1,i2)


    
    print(datetime.datetime.now())
    e = datetime.datetime.now()
    all_t = e-s








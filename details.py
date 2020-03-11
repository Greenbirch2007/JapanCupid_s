import requests
import re
import urllib
import time
from requests.exceptions import RequestException  #用于捕捉异常
from multiprocessing import Pool
import random

import os

# 通过算法优势把图片给弄下来
#关键是找到id










ln = os.getcwd()
url__p = 'https://cdn.japancupid.com/memphoto/Photo4/big/2883065.jpg'
urllib.request.urlretrieve(url__p, '{0}/{1}.jpg'.format(ln,url__p[-11:-4]+url__p[-22:-16]))




#! -*- coding:utf-8 -*-


import datetime
import re
import os
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import xlrd
from xlrd import xldate_as_tuple
import datetime
import pymysql
import requests
from lxml import etree
from requests.exceptions import RequestException

def call_page(url):

    driver.get(url)
    # 弄一个模拟登陆背
    driver.find_element_by_xpath('/html/body/div[1]/div/a').click()


    time.sleep(20)
    driver.find_element_by_xpath('//*[@id="form-login-email"]').clear()
    driver.find_element_by_xpath('//*[@id="form-login-email"]').send_keys("291109028@qq.com")#用户名

    time.sleep(20)

    driver.find_element_by_xpath('//*[@id="form-login-password"]').clear()
    driver.find_element_by_xpath('//*[@id="form-login-password"]').send_keys("123456aaa")# 密码
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/form/button').click()

    time.sleep(90)



    # 选择年龄 解决下拉列表的问题

    opt = driver.find_element_by_name('age_min')
    Select(opt).select_by_visible_text('18')


    opt = driver.find_element_by_name('age_max')
    Select(opt).select_by_visible_text('20')




    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="form-quick-search"]/div/button').click()

    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[6]/a/div/div/div/div[2]/svg').click()






    html = driver.page_source


    return html


def parse_pages(html):

    selector = etree.HTML(html)
    station_Name = selector.xpath('//*[@id="station"]/ul/li/a/text()')
    city_name = selector.xpath('//*[@id="cat-pass"]/p/a[4]/text()')
    railwayName = selector.xpath('//*[@id="title"]/h2/text()')
    f_city = len(station_Name)*city_name
    f_railwayName= len(station_Name)*railwayName
    for i1,i2,i3 in zip(station_Name,f_railwayName,f_city):
        big_list.append((i1+"--"+i2+"--"+i3))








def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))

       # # if 去掉表头
       # if rowNum > 0:


    return dataFile


def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")



if __name__ == '__main__':

    driver = webdriver.Chrome()
    url = 'https://www.japancupid.com/'

    big_list = []
    html = call_page(url)
    # parse_pages(html)
    #
    # # 上面完成第一次登陆，后面就不再登陆
    # lpath = os.getcwd()
    # for url in tokyo_url:
    #     driver.get(url)
    #     # 弄一个模拟登陆背
    #     time.sleep(1)
    #     html = driver.page_source
    #     parse_pages(html)
    #
    #
    #     print(big_list)
    #
    #
    # text_save('{0}\\t.xlsx'.format(lpath),big_list)
    # driver.quit()




#     lpath = '/root/YD_mp3Cards/日语mp3单词库'
#     # lpath =  os.getcwd()
#     excelFile = '{0}/mp_jans.xlsx'.format(lpath)
#     full_items = read_xlrd(excelFile=excelFile)
#     for single_name in full_items:
#         print(single_name)
#         url = 'https://www.youdao.com/w/jap/{0}/#keyfrom=dict2.top'.format(single_name[0])
#         html = call_page(url)
#
#         patt = re.compile('<a href="#" title="发音" class="sp dictvoice voice-js log-js" data-rel="(.*?)" data-4log="dict.basic.jc.voice"></a>',re.S)
#         mp3_c = re.findall(patt, html)
#         try:
#             big_list = []
#             if len(mp3_c) != 0:
#                 for item in mp3_c:
#                     f_url = "".join(item.split("amp;"))
#                     big_list.append('https://dict.youdao.com/dictvoice?audio={0}'.format(f_url))
#
#             for mp3_url in big_list:
#                 res = requests.get(mp3_url)
#
#                 music = res.content
#
#                 with open(r'{0}/{1}.mp3'.format(lpath,single_name[1]), 'ab') as file:  # 保存到本地的文件名
#                     file.write(res.content)
#                     file.flush()
#                     time.sleep(0.3)
#
#         except:
#
#             pass



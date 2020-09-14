# select方法主要有三类
#
# select_by_index(self, index)    　　 #以index属性值来查找匹配的元素并选择；
# select_by_value(self, value)        #以value属性值来查找该option并选择；
# select_by_visible_text(self, text)  #以text文本值来查找匹配的元素并选择；
# first_selected_option(self)         #选择第一个option 选项 ；


#使用以上三类方法做个简单的练习

from selenium.webdriver.support.select import Select
from selenium import webdriver
from time import sleep
'/html/body/select'
driver = webdriver.Chrome()
driver.get("C:\\Users\\Administrator\\Desktop\\JapanCupid_s\\selenium.下拉框操作（select_by）\\index.html")
opt = driver.find_element_by_name('辛弃疾')
Select(opt).select_by_visible_text('醉里挑灯看剑，梦回吹角连营。')
sleep(1)
# Select(opt).select_by_index(1)
# sleep(1)
# Select(opt).select_by_value('03')

driver.quit()
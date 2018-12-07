#!/user/bin/python
#-*- coding:utf-8 -*-
#Author:一土小亘兄
#@Time: 17:03
import time
from selenium import webdriver
####谷歌登陆fw
def gugelog():
    dr = webdriver.Chrome()
    dr.get('https://30.1.1.1:8889')
    time.sleep(1)
    dr.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/ul/li[2]/input').send_keys('Bane@7766')
    a = dr.find_elements_by_class_name("nobody")
    for i in a:
        h = i.get_attribute('src')
        dr.find_element_by_id("input1").send_keys(f'{h[-5]}')
        time.sleep(0.1)
    time.sleep(1)
    dr.find_element_by_xpath('/html/body/table/tbody/tr/td/div/form/ul/li[4]/input[1]').click()
    try:
        dr.switch_to_alert().accept()
    except:
        pass
    return dr



#####切换至pppoe接口操作界面
def qhppp(dr):
    dr.switch_to.frame('left')  ####左边框架
    dr.find_element_by_xpath('//*[@id="02_image"]').click()
    dr.find_element_by_xpath('//*[@id="Interface"]/span').click()
    dr.switch_to.default_content()  ####回到默认框架
    dr.switch_to.frame('subnav')  ####上面操作栏框架
    time.sleep(1)
    dr.find_element_by_xpath('//*[@id="nav_5"]').click()
    dr.switch_to.default_content()
    dr.switch_to.frame('main')  ####记录列表框架
    time.sleep(1)
    return dr

# import xlrd
#
# f=xlrd.open_workbook('pppoe.xls')
# sheet=f.sheets()[0]
# for i in range (0,3):
#     b=sheet.row_values(i)







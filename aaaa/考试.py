#！/usr/bin/env python
#-*- encoding=utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
import selenium.webdriver.support.ui as ui
import unittest
import re
import requests
import pymysql
import xlwt
import xlrd
#qq空间
class qq(unittest.TestCase):

    # def test_登录(self):
    #     dr = webdriver.Chrome()
    #     dr.get('https://qzone.qq.com/')
    #     sleep(2)
    #     dr.switch_to.frame('login_frame')
    #     sleep(2)
    #     dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
    #     sleep(2)
    #     dr.find_element_by_xpath('//*[@id="u"]').send_keys('1874694392222')
    #     sleep(2)
    #     dr.find_element_by_xpath('//*[@id="p"]').send_keys('zzz25210')
    #     dr.find_element_by_xpath('//*[@id="login_button"]').click()
    #     sleep(2)
    #     wd1 = dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
    #     dr.switch_to_frame(wd1)
    #     sleep(2)
    #     start = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
    #     sleep(2)
    #     while True:
    #         i=150
    #         ActionChains(dr).drag_and_drop_by_offset(start,i+5,0).perform()
    #         sleep(1)
    #         wd = dr.find_element_by_xpath('//*[@id="err_m"]').text
    #         self.assertEqual(wd,'你输入的帐号或密码不正确，请重新输入。')


    def test_2(self):
        dr = webdriver.Chrome()
        dr.get('https://qzone.qq.com/')
        sleep(2)
        dr.switch_to.frame('login_frame')
        sleep(2)
        dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        sleep(2)
        dr.find_element_by_xpath('//*[@id="u"]').send_keys('1874694392')
        sleep(2)
        dr.find_element_by_xpath('//*[@id="p"]').send_keys('zzzz25210')
        dr.find_element_by_xpath('//*[@id="login_button"]').click()
        wd=dr.find_element_by_xpath('//*[@id="top_head_title"]/span[1]').text
        print(wd)
        # self.assertEqual(wd,'Yakult的QQ空间')

a = qq()
a.test_2()

# 京东
# class jd(unittest.TestCase):
#     def test_购物车(self):
#         dr = webdriver.Chrome()
#         dr.get('https://www.jd.com/')
#         sleep(2)
#         dr.find_element_by_xpath('//*[@id="key"]').send_keys('纪梵希')
#         sleep(2)
#         dr.find_element_by_xpath('//*[@id="search"]/div/div[2]/button/i').click()
#         sleep(2)
#         dr.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[2]/div/div[3]/a/em').click()
#         sleep(2)
#         wd = dr.window_handles
#         dr.switch_to.window(wd[-1])
#         dr.find_element_by_xpath('//*[@id="InitCartUrl"]').click()
#         sleep(2)
#         wd = dr.find_element_by_xpath('//*[@id="succeed"]/div[1]/h3').text
#         self.assertEqual(wd,'商品已成功加入购物车！')
#
#
# if __name__ == '__main__':
#     unittest.main()
# a = jd()
# a.test_购物车()

#boss直聘
# url = 'https://www.zhipin.com/job_detail/?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&scity=101010100&industry=&position='
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
# response = requests.get(url=url,headers=head,verify=False)
# html = response.content.decode('utf-8')
# patt1 = re.compile('<div class="job-title">(.*?)</div>')
# patt2 = re.compile('<span class="red">(.*?)</span>')
# patt3 = re.compile('<div class="info-detail"></div>(.*?)</p>',re.S)
# patt4 = re.compile('custompage" target="_blank">(.*?)</a></h3>',re.S)
# items1 = patt1.findall(html)
# items2 = patt2.findall(html)
# items3 = patt3.findall(html)
# items4 = patt4.findall(html)
# f = xlwt.Workbook()
# sheet = f.add_sheet('boss')
# for i,j in enumerate(items1):
#     j=j.replace('&nbsp;','')
#     sheet.write(i,0,j)
#     f.save('bosss.xls')
#
# for i,j in enumerate(items2):
#     sheet.write(i,1,j)
#     f.save('bosss.xls')
#
# for j,i in enumerate(items3):
#     i=i.replace('</a>','')
#     i=i.replace('</h3>','')
#     i=i.replace('<p>','')
#     i = i.replace('<em class="vline"></em>','')
#     i=i.replace('<em class="vline"></em>','')
#     i=i.strip()
#     sheet.write(j, 2, i)
#     f.save('bosss.xls')
#
#
# for i,j in enumerate(items4):
#     j=j.replace('','')
#     sheet.write(i, 3, j)
#     f.save('bosss.xls')

# aaa = pymysql.connect(host='192.168.0.114',
#                       user='root',
#                       password='123456',
#                       port=3306,
#                       charset='utf8')
# a = aaa.cursor()
# # a.execute('create database boss;')
# a.execute('use boss;')
# a.execute('create table boss1(职位 char(255),薪资 char(255),地址 char(255),公司 char(255));')
# f = xlrd.open_workbook('bosss.xls')
# sheet = f.sheets()[0]
# b = sheet.nrows
# for i in range(b):
#     c = sheet.row_values(i)
#     # print(c)
#     a.execute('insert into boss1 values("{}","{}","{}","{}");'.format(c[0],c[1],c[2],c[3]))
#     aaa.commit()
# a.execute('select * from biao;')
# for i in a.fetchall():
#     print(i)

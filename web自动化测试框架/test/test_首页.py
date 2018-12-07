#!/usr/bin/env python
#! -*- encoding=utf -*-
from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from web自动化测试框架.config.请求_网址 import 请求URL
import logging
from selenium.webdriver.common.action_chains import  ActionChains


class 测试(unittest.TestCase):
    tes = 请求URL().网址登录('http://www.moore.ren/')

    def test_1(self):
        self.tes.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/a[1]').click()
        wd = self.tes.window_handles
        self.tes.switch_to.window(wd[-1])
        sleep(2)
        wd1=self.tes.title
        self.assertEqual(wd1,'摩尔精英官网-让中国没有难做的芯片')


    def test_2(self):
        self.tes.find_element_by_xpath('//*[@id="searchform"]/input[1]').send_keys('软件测试')
        sleep(2)
        self.tes.find_element_by_xpath('//*[@id="search-submit"]').click()
        wd = self.tes.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/span[2]').text
        self.assertEqual(wd,'软件测试')


    def test_3(self):
        self.tes.find_element_by_xpath('//*[@id="user-nomal"]/div[2]/ul/li[2]/a').click()
        sleep(2)
        self.tes.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/ul/li[1]/div[1]/div[2]/h3/a').click()
        wd = self.tes.window_handles
        self.tes.switch_to.window(wd[-1])
        wd1 = self.tes.title
        self.assertEqual(wd1,'深圳市紫光同创电子有限公司-深圳市紫光同创电子有限公司招聘-深圳市紫光同创电子有限公司招聘-摩尔精英招聘')
        self.tes.close()
        # wd2 = self.tes.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/ul').find_elements_by_tag_name('li')
        # for i in wd2:
        #     ActionChains(self.tes).move_to_element(i).perform()
        #     sleep(2)


    def test_4(self):
        self.tes.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[1]/div[1]/ul/li[3]/i').click()
        sleep(2)
        self.tes.find_element_by_xpath('//*[@id="see-more"]').click()
        sleep(2)
        self.tes.find_element_by_xpath('//*[@id="mycity"]/span').click()
        sleep(2)
        self.tes.find_element_by_xpath('//*[@id="supplychain"]/span').click()
        self.tes.find_element_by_xpath('//*[@id="jobcustomize"]/div[4]/div[1]/ul/li/ul/li[16]').click()
        sleep(2)
        self.tes.find_element_by_xpath('')










# if __name__ == '__main__':
#     unittest.main()
a = 测试()
a.test_3()
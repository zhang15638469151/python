#!/usr/bin/env python
#! -*- encoding=utf -*-
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from web自动化测试框架.config.请求_网址 import 请求URL

class 测试(unittest.TestCase):
    tes = 请求URL().网址登录('http://www.moore.ren/')

    def test_1(self):
        wd = self.tes.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[4]/div').find_elements_by_tag_name('li')
        wd1 = self.tes.window_handles
        sleep(2)
        self.tes.switch_to.window(wd1[1])
        for i in wd:
            i.click()
            sleep(2)
            self.tes.switch_to.window(wd1[-1])
            self.assertEqual(self.tes.title,'"{}"半导体职位-半导体招聘-半导体人才网-摩尔精英招聘'.format(i.text))
            self.tes.switch_to.window(wd1[1])






a = 测试()
a.test_1()
# if __name__ == '__main__':
#     unittest.main()








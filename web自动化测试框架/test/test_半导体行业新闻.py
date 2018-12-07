#!/usr/bin/env python
#! -*- encoding=utf -*-
import unittest
from time import sleep
from selenium import webdriver
from web自动化测试框架.config.请求_网址 import 请求URL

class 测试(unittest.TestCase):
    tes = 请求URL().网址登录('http://www.moore.ren/')

    def test_1(self):
        self.tes.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/a[8]').click()
        wd = self.tes.window_handles
        sleep(2)
        self.tes.switch_to.window(wd[-1])
        a = self.tes.title
        self.assertEqual(a,'摩尔芯闻-全球半导体内参-半导体新闻-摩尔半导体指数新鲜发布')





if __name__ == '__main__':
    unittest.main()




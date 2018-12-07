from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from web自动化测试框架.config.请求_网址 import 请求URL


class 测试(unittest.TestCase):
    tes = 请求URL().网址登录('http://www.moore.ren/')

    def test_1(self):
        self.tes.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div/div/li/a').click()
        self.assertEqual(self.tes.title,'我的简历-摩尔精英')
        self.tes.back()


    def test_2(self):
        self.tes.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div/li[2]/a').click()
        self.assertEqual(self.tes.title,'投递箱')
        sleep(2)
        self.tes.back()

    def test_3(self):
        self.tes.find_element_by_xpath('//*[@id="login-name"]/a').click()
        self.tes.find_element_by_xpath('//*[@id="top_right"]/li[1]/a').click()
        self.assertEqual(self.tes.title, '个人用户修改密码')
        sleep(2)
        self.tes.back()



    def test_4(self):
        self.tes.find_element_by_xpath('//*[@id="login-name"]/a').click()
        self.tes.find_element_by_xpath('//*[@id="top_right"]/li[2]/a').click()
        sleep(2)
        self.assertEqual(self.tes.title, '摩尔精英招聘-专业的半导体招聘平台-半导体人才网-半导体工作')



if __name__ == '__main__':
    unittest.main()
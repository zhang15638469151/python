#!/usr/bin/env python
#! -*- encoding=utf -*-

from time import sleep
from selenium import webdriver


class 请求URL():
    def 网址登录(self,a):
        dr = webdriver.Chrome()
        dr.get(a)
        dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
        wd = dr.window_handles
        sleep(2)
        dr.switch_to.window(wd[1])
        sleep(2)
        dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('15638469151')
        sleep(2)
        dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('zzzzz25210')
        sleep(2)
        dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').click()
        sleep(10)
        return dr


    def 网址2(self,b):
        pass


# a = 请求URL()
# a.网址登录('http://www.moore.ren/')
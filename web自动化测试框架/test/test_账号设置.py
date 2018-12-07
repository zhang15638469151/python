from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from web自动化测试框架.config.请求_网址 import 请求URL


class 测试(unittest.TestCase):
    tes = 请求URL().网址登录('http://www.moore.ren/')

    def test_1(self):
        self.tes.find_element_by_xpath('//*[@id="login-name"]/a').click()
        self.tes.find_element_by_xpath('//*[@id="top_right"]/li[1]/a').click()
        sleep(2)
        self.tes.find_element_by_xpath('//*[@id="newpasswordform"]/div/div[2]/div/input').send_keys('zzzzzz25210')
        sleep(2)
        self.tes.find_element_by_xpath('//*[@id="firstpassword"]').send_keys('zzzzz25210')
        sleep(2)
        self.tes.find_element_by_xpath('//*[@id="newpasswordform"]/div/div[7]/div/input').send_keys('zzzzz25210')
        self.tes.find_element_by_xpath('//*[@id="newpasswordform"]/div/a').click()
        sleep(2)
        wd = self.tes.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/h1').text
        sleep(2)
        self.assertEqual(wd,'恭喜你，密码修改成功!')
        sleep(2)



    def test_2(self):
        self.tes.find_element_by_xpath('//*[@id="login-name"]/a').click()
        self.tes.find_element_by_xpath('//*[@id="top_right"]/li[1]/a').click()
        sleep(2)
        self.tes.find_element_by_xpath('/html/body/div[2]/div/div/div/dl/dd[2]/a').click()
        self.tes.find_element_by_xpath('//*[@id="emailadd"]').click()
        sleep(2)
        self.tes.find_element_by_xpath('//*[@id="modify-mail-box"]/div[2]/input').send_keys('1564694392@163.com')
        sleep(2)
        self.tes.find_element_by_xpath('//*[@id="modify-mail-box"]/div[3]/a[1]').click()
        self.assertEqual(self.tes.title,'账号绑定')



    def test_3(self):
        self.tes.find_element_by_xpath('//*[@id="login-name"]/a').click()
        self.tes.find_element_by_xpath('//*[@id="top_right"]/li[1]/a').click()
        sleep(2)
        self.tes.find_element_by_xpath('/html/body/div[2]/div/div/div/dl/dd[2]/a').click()
        self.tes.find_element_by_xpath('/html/body/div[2]/div/div/div/dl/dd[3]/a').click()
        sleep(2)
        self.tes.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[4]/div/div/div/input').send_keys('163.com')
        sleep(2)
        self.tes.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/a').click()
        wd = self.tes.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/h1').text
        self.assertEqual(wd,'恭喜你，屏蔽邮箱成功!')

# if __name__ == '__main__':
#     unittest.main()



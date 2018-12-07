from appium import webdriver
import time
import unittest
#启动设备，连接设备

desired_caps = {'platformName':'Android',
                # 'platformVersion':'5.0',
                'deviceName':'127.0.0.1:62001',
                'appPackage':'com.netease.cloudmusic',
                'appActivity':'activity.LoadingActivity'}

#
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
#
# # driver.find_element_by_name('浙大教室').click()
# # time.sleep(3)
# driver.find_element_by_id('net.crigh.cgapp_schedule:id/editLoginUserName').send_keys('1138100001')
# time.sleep(2)
# driver.find_element_by_id('net.crigh.cgapp_schedule:id/editLoginUserPas').send_keys('123456')
# time.sleep(2)
# driver.find_element_by_id('net.crigh.cgapp_schedule:id/btnLogin').click()
# time.sleep(2)

# time.sleep(2)
# driver.find_element_by_id('com.netease.cloudmusic:id/mx').click()
# time.sleep(2)
# driver.find_element_by_id('com.netease.cloudmusic:id/py').click()
# time.sleep(2)
# driver.find_element_by_id('com.netease.cloudmusic:id/abx').click()
# time.sleep(3)
# driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
# time.sleep(3)
# driver.find_element_by_id('com.netease.cloudmusic:id/i4').send_keys('15638469151')
# time.sleep(3)
# driver.find_element_by_id('com.netease.cloudmusic:id/i2').send_keys('zzzz25210')
# time.sleep(3)
# driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
# driver.quit()


# time.sleep(3)
# print("123")
# driver.find_element_by_id("com.netease.cloudmusic:id/mx").click()
# time.sleep(3)
#
# driver.find_element_by_id('com.netease.cloudmusic:id/py').click()
# time.sleep(3)
#
# driver.find_element_by_id('com.netease.cloudmusic:id/abx').click()
# time.sleep(3)
#
# driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
# time.sleep(3)
#
# driver.find_element_by_id('com.netease.cloudmusic:id/i4').send_keys('15638469151')
# time.sleep(3)
# driver.find_element_by_id('com.netease.cloudmusic:id/i2').send_keys('zzzz25210')
# time.sleep(3)
# driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
# driver.quit()




class wangyiyun(unittest.TestCase):

    # def aaa(self):
    #     desired_caps = {'platformName': 'Android',
    #                     # 'platformVersion':'5.0',
    #                     'deviceName': '127.0.0.1:62001',
    #                     'appPackage': 'net.crigh.cgapp_schedule',
    #                     'appActivity': 'activity.login.LoginActivity'}
    #     driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



    def test_登录(self):
        driver.find_element_by_id("com.netease.cloudmusic:id/mx").click()
        time.sleep(3)

        driver.find_element_by_id('com.netease.cloudmusic:id/py').click()
        time.sleep(3)

        driver.find_element_by_id('com.netease.cloudmusic:id/abx').click()
        time.sleep(3)

        driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
        time.sleep(3)

        driver.find_element_by_id('com.netease.cloudmusic:id/i4').send_keys('15638469151')
        time.sleep(3)
        driver.find_element_by_id('com.netease.cloudmusic:id/i2').send_keys('zzzz25210')
        time.sleep(3)
        driver.find_element_by_id('com.netease.cloudmusic:id/py').click()
        time.sleep(2)
        wd = driver.find_element_by_id('com.netease.cloudmusic:id/ac2').text
        self.assertEqual(wd,'张腾i')




if __name__ == '__main__':
    unittest.main()





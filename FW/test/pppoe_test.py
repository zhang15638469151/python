#!/user/bin/python
#-*- coding:utf-8 -*-
#Author:一土小亘兄
#@Time: 17:08
from selenium import webdriver
import time,re
import paramiko

import unittest
class pppoe(unittest.TestCase):
    def setUp(self):
        self.dr = login.gugelog()
##新建功能
    # def test_101(self):
    #     dr=self.dr
    #     num = create_ppp.create_new(dr,1)
    #     # print(num)
    #     time.sleep(8)
    #     de=sshfw.sshfw('ifconfig')
    #     print(de)
    #     self.assertIn(f'ppp{num}',de)
    #
    # def test_102(self):
    #     dr=self.dr
    #     num = create_ppp.create_new(dr,2)
    #     # print(num)
    #     time.sleep(8)
    #     de=sshfw.sshfw('ifconfig')
    #     print(de)
    #     self.assertIn(f'ppp{num}',de)
    #
    # def test_103(self):
    #     dr = self.dr
    #     num=create_ppp.create_new(dr,3)
    #     err=dr.switch_to_alert()
    #     print(err.text)
    #     self.assertEqual(err.text,'描述过长！')
    #
    #
    # def test_104(self):
    #     dr = self.dr
    #     num=create_ppp.create_new(dr,4)
    #     err=dr.switch_to_alert()
    #     print(err.text)
    #     self.assertEqual(err.text,'描述不能包含非法字符(#)！')
    #
    # def test_105(self):
    #     dr = self.dr
    #     num=create_ppp.create_new(dr,5)
    #     err=dr.switch_to_alert()
    #     print(err.text)
    #     self.assertEqual(err.text,'绑定接口不能够为空')
    #
    # def test_106(self):
    #     dr = self.dr
    #     num = create_ppp.create_new(dr, 6)
    #     err=dr.switch_to_alert()
    #     print(err.text)
    #     self.assertEqual(err.text,'密码不允许为空！')
    #
    # def test_107(self):
    #     dr = self.dr
    #     num = create_ppp.create_new(dr, 7)
    #     err=dr.switch_to_alert()
    #     print(err.text)
    #     self.assertEqual(err.text,'密码中含有非法字符！')
    #
    # def test_108(self):
    #     dr = self.dr
    #     num = create_ppp.create_new(dr, 8)
    #     err=dr.switch_to_alert()
    #     print(err.text)
    #     self.assertEqual(err.text,'密码长度不能超过64！')
    #
    # def test_109(self):
    #     dr = self.dr
    #     num = create_ppp.create_new(dr, 9)
    #     err=dr.switch_to_alert()
    #     print(err.text)
    #     self.assertEqual(err.text,'用户名不允许为空！')
    #
    # def test_110(self):
    #     dr = self.dr
    #     num = create_ppp.create_new(dr, 9)
    #     err=dr.switch_to_alert()
    #     print(err.text)
    #     self.assertEqual(err.text,'用户名中含有非法字符！')
    #
    # def test_111(self):
    #     dr = self.dr
    #     num = create_ppp.create_new(dr, 9)
    #     err=dr.switch_to_alert()
    #     print(err.text)
    #     self.assertEqual(err.text,'用户名长度不能超过64！')

###查询功能
    #
    # def test_201(self):
    #     dr = self.dr
    #     num = create_ppp.find_port(dr, 38)
    #     err=dr.switch_to_alert()
    #     self.assertEqual(err.text,num)
    #
    # def test_202(self):
    #     dr = self.dr
    #     num = create_ppp.find_port(dr, 39)
    #     err=dr.switch_to_alert()
    #     self.assertEqual(err.text,num)
    #
    # def test_203(self):
    #     dr = self.dr
    #     num = create_ppp.find_port(dr, 40)
    #     err=dr.switch_to_alert()
    #     self.assertEqual(err.text,num)
    #
    # def test_204(self):
    #     dr = self.dr
    #     num = create_ppp.find_port(dr, 41)
    #     err=dr.switch_to_alert()
    #     self.assertEqual(err.text,num)
    #
    # def test_205(self):
    #     dr = self.dr
    #     num = create_ppp.find_port(dr, 42)
    #     err=dr.switch_to_alert()
    #     self.assertEqual(err.text,num)
    #
    # def test_206(self):
    #     dr = self.dr
    #     num = create_ppp.find_port(dr, 43)
    #     err=dr.switch_to_alert()
    #     self.assertEqual(err.text,num)
    #
    # def test_207(self):
    #     dr = self.dr
    #     num = create_ppp.find_port(dr, 44)
    #     err=dr.switch_to_alert()
    #     self.assertEqual(err.text,num)
    #
    # def test_208(self):
    #     dr = self.dr
    #     num = create_ppp.find_port(dr, 45)
    #     err=dr.switch_to_alert()
    #     self.assertEqual(err.text,num)
    #
    # def test_209(self):
    #     dr = self.dr
    #     num = create_ppp.find_port(dr, 46)
    #     err=dr.switch_to_alert()
    #     self.assertEqual(err.text,num)
    #
    # def test_210(self):
    #     dr = self.dr
    #     num = create_ppp.find_port(dr, 47)
    #     err=dr.switch_to_alert()
    #     self.assertEqual(err.text,num)
    # #
    # def test_211(self):
    #     dr = self.dr
    #     num = create_ppp.find_port(dr, 48)
    #     err=dr.switch_to_alert()
    #     self.assertEqual(err.text,num)

    # def test_212(self):
    #     dr = self.dr
    #     num = create_ppp.find_true(dr, 31)
    #     print(num)
    #     self.assertEqual(num[0],num[1])

    # def test_213(self):
    #     dr = self.dr
    #     num = create_ppp.find_true(dr, 32)
    #     print(num)
    #     self.assertEqual(num[1][0],num[0][0])

    # def test_214(self):
    #     dr = self.dr
    #     num = create_ppp.find_true(dr, 33)
    #     print(num)
    #     if num[0]==[]:
    #         self.assertEqual([],num[1])
    #     elif num[1]==[]:
    #         for i in num[0]:
    #             self.assertNotIn('30.1.1.1',i)
    #     else:
    #         numm=[]
    #         for i in num[0]:
    #             if '30.1.1.1' in i:
    #                 numm.append(i)
    #         self.assertEqual(numm,num[1])
    #
    # def test_215(self):
    #     dr = self.dr
    #     num = create_ppp.find_true(dr, 34)
    #     print(num)
    #     if num[0]==[]:
    #         self.assertEqual([],num[1])
    #     elif num[1]==[]:
    #         for i in num[0]:
    #             self.assertNotIn('255.255.255.0',i)
    #     else:
    #         numm=[]
    #         for i in num[0]:
    #             if '30.1.1.1' in i:
    #                 numm.append(i)
    #         self.assertEqual(numm,num[1])

    # def test_216(self):
    #     dr = self.dr
    #     num = create_ppp.find_true(dr, 35)
    #     print(num)
    #     self.assertEqual(num[0],num[1])
    #
    # def test_217(self):
    #     dr = self.dr
    #     num = create_ppp.find_true(dr, 36)
    #     print(num)
    #     self.assertEqual([],num[1])






    def tearDown(self):
        self.dr.quit()

# if __name__=="__main__":
#     unittest.main()
#


def main():## 通过加载要测试的类来测试
    ''' 创建测试集'''
    suite1 = unittest.TestLoader().loadTestsFromTestCase(pppoe)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(Link_ce_1)
    alltests = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return alltests

main()



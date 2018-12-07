#/usr/bin/env Python
#-*- coding=utf-8 -*-
#接口测试：发送请求，验证响应是否符合需求的过程
#Python中发送HTTP请求的模块：requests
#assert：Python提供的断言处理
import requests
import unittest           #Python自带的，做单元测试的自动化测试框架


def test(a):
    # a=input('地区:')
    a = '北京'
    url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
    querystring = {'filterInput':"{}".format(a)}
    head = {'cookie':'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'}
    response = requests.get(url=url,headers=head,params=querystring)
    b = response.json()
    print(b)
    assert b['code'] == 0


#断言:如果断言成功则不显示，断言错误会报错
# assert b['code']==0
# assert b['code']==1










#ass 学校(unittest.TestCase):
# cl
#     def setUp(self):           #setup作用：初始化测试环境    在每次执行测试用例前执行（保证每一个用例在相同的环境下去执行）
#         print(123)
#
#
#     def tearDown(self):        #teardown：清理环境的，每次用例执行之后执行
#         print(567)
#
#
#     def test_1(self):          #测试用例：必须以test开头
#         print('a')
#
#
#     def test_2(self):
#         print('b')
#
#
#
# unittest.main()















import unittest
import requests
import HTMLTestRunnertest
import HTMLTestRunne
import time
import xlrd

def tes(a):
    url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
    querystring = {'filterInput': "{}".format(a)}
    head = {
        'cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'}
    response = requests.get(url=url, headers=head, params=querystring)
    b = response.json()
    return b


class 学校(unittest.TestCase):

    def tes_数据(self):
        shuju=[]
        f = xlrd.open_workbook('test.xls')
        sheet = f.sheets()[0]
        num = sheet.nrows
        for i in range(1,num):
            aaa=sheet.row_values(i)
            shuju.append(aaa)
        return shuju



    def test_1(self):          #测试用例：必须以test开头
        shuju = self.tes_数据()
        b=tes(shuju[0][0])
        self.assertEqual(b['code'],int(shuju[0][1]))
        # self.assertEqual(b['data'][0]['schoolName'],'北京七中')

    def test_2(self):
        shuju = self.tes_数据()
        b=tes(shuju[1][0])
        self.assertEqual(b['code'],shuju[1][1])



    def test_3(self):
        shuju = self.tes_数据()
        b=tes(shuju[2][0])
        # self.assertEqual(b['msg'],'学校')
        self.assertEqual(len(b['data']),int(shuju[2][2]))

# # if __name__=='__main__':
# #
# #     suit = unittest.TestSuite()                 #生成测试报告，创建一个测试套件
# #     # suit.addTest(学校('test_1'))                 #添加测试用例：将测试用例添加到测试套件中
# #     # suit.addTest(学校('test_2'))
# #     # suit.addTest(学校('test_3'))
# #     suit.addTest(unittest.makeSuite(学校))        #将一个类中的所有测试用例添加到测试套件中
# #     now = time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
# #     f = open('abcd.html','wb')
# #     runner = HTMLTestRunne.HTMLTestRunner(tester='张',
# #                                                description='测试结果如下:',
# #                                                title='好分数测试报告',
# #                                                stream=f,)
# #     runner.run(suit)
# #     f.close()



if __name__=='__main__':

    suit = unittest.TestSuite()                 #生成测试报告，创建一个测试套件
    # suit.addTest(学校('test_1'))                 #添加测试用例：将测试用例添加到测试套件中
    # suit.addTest(学校('test_2'))
    # suit.addTest(学校('test_3'))
    suit.addTest(unittest.makeSuite(学校))        #将一个类中的所有测试用例添加到测试套件中
    now = time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
    f = open('abcde.html','wb')
    runner = HTMLTestRunnertest.HTMLTestRunner(tester='张',
                                               description='测试结果如下:',
                                               title='好分数测试报告',
                                               stream=f)
    runner.run(suit)
    f.close()









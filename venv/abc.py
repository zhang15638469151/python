#！/usr/bin/env python
# -*- encoding=utf-8 -*-
import unittest
import requests
import HTMLTestRunnertest
import time
import xlrd


class 好分数(unittest.TestCase):

    def 网址(self,a):
        url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
        querystring = {'filterInput': "{}".format(a)}
        head = {'cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'}
        response = requests.get(url=url,headers=head,params=querystring)
        b = response.json()
        return b


    def 数据(self):
        shuju = []
        f=xlrd.open_workbook('test.xls')
        sheet=f.sheets()[0]
        num=sheet.nrows
        for i in range(1,num):
            a = sheet.row_values(i)
            shuju.append(a)
        return shuju



    def test_1(self):
        shuju = self.数据()
        b=self.网址(shuju[0][0])
        self.assertEqual(b['code'],int(shuju[0][1]))
        # self.assertEqual(b['data'],int(shuju[0][2]))



    def test_2(self):
        shuju = self.数据()
        b = self.网址(shuju[1][0])
        self.assertEqual(b['code'],int(shuju[1][1]))
        self.assertNotIn('schoolName',b['data'])



    def test_3(self):
        shuju = self.数据()
        b = self.网址(shuju[2][0])
        self.assertEqual(b['code'],int(shuju[2][1]))
        self.assertNotEqual(b['data'],int(shuju[2][2]))

if __name__=='__main__':
    unittest.main()



if __name__=='__main__':
    suit = unittest.TestSuite()
    suit.addTest(unittest.makeSuite(好分数))
    now = time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
    f = open('zhang.html','wb')
    runner = HTMLTestRunnertest.HTMLTestRunner(tester='张腾',
                                               description='测试结果如下:',
                                               title='好分数测试报告',
                                               stream=f)
    runner.run(suit)
    f.close()












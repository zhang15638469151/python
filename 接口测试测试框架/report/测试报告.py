#!/usr/bin/env python
# -*- encoding=utf-8
import unittest
from 接口测试测试框架.report import HTMLTestRunnertest
import time

def run_多(aa):
    suit = unittest.TestSuite()
    for i in aa:
        discover = unittest.defaultTestLoader.discover(r'..\test', pattern='{}.py'.format(i.strip()))
        suit.addTest(discover)
    now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
    f = open('地址.html', 'wb')
    runner = HTMLTestRunnertest.HTMLTestRunner(tester='张腾',
                                               description='测试结果如下:',
                                               title='常用地址测试报告',
                                               stream=f)
    runner.run(suit)
    f.close()

#!/usr/bin/env python
# -*- encoding=utf-8
import unittest
import HTMLTestRunnertest
import time
import re
import xlrd
from 接口测试测试框架.config.地址_接口 import 地址_查询
from 接口测试测试框架.data.读取数据 import 数据
from 接口测试测试框架.test.test_地址 import 地zhi
from 接口测试测试框架.report.测试报告 import run_多

class Test_run():

    def run_多个(self,aa):
        run_多(aa)

    def run_all(self,aa):
        run_多(aa)


if __name__=='__main__':
    run=Test_run()
    with open('run.txt','r') as f:
        aa = f.readlines()
        print(aa)
    if 'all' in aa:
        aa = ['test*']
        run.run_all(aa)
    else:
        run.run_多个(aa)




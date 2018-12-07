#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from 接口测试测试框架.config.地址_接口 import 地址_查询
from 接口测试测试框架.data.常用收货地址数据 import 数据
import json
class 地zhi(unittest.TestCase):
    tes_地址=地址_查询().常用地址
    shuju=数据()
    def test_1(self):
        b=self.tes_地址(int(self.shuju[0][0]))
        b = json.loads(b)
        self.assertEqual(b['code'],str(int(self.shuju[0][1])))


    def test_2(self):

        b=self.tes_地址(self.shuju[1][0])
        self.assertIn('Struts Problem Report',b)


    def test_3(self):

        b=self.tes_地址(self.shuju[2][0])
        self.assertIn('Struts Problem Report', b)


    def test_4(self):
        b=self.tes_地址(int(self.shuju[3][0]))
        b = json.loads(b)
        self.assertEqual(b['code'],str(int(self.shuju[3][1])))

if __name__=='__main__':
    unittest.main()

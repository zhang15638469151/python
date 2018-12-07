#!/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest
from 接口测试测试框架.config.学校_接口 import 学校_查询
from 接口测试测试框架.data.读取数据 import 数据


class 学校(unittest.TestCase):
    tes_学校=学校_查询().学校_快查
    shuju=数据()
    def test_1(self):
        b=self.tes_学校(self.shuju[0][0])
        self.assertEqual(b['code'],int(self.shuju[0][1]))


    def test_2(self):

        b=self.tes_学校(self.shuju[1][0])
        self.assertEqual(b['code'],self.shuju[1][1])


    def test_3(self):

        b=self.tes_学校(self.shuju[2][0])
        self.assertEqual(len(b['data']),int(self.shuju[2][2]))


# if __name__=='__main__':
#     unittest.main()
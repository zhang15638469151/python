#!/usr/bin/env python
#! -*- encoding=utf -*-

import xlrd

def test_数据():
    shuju = []
    f = xlrd.open_workbook('a.xls')
    sheet = f.sheets()[0]
    num = sheet.nrows
    for i in range(1, num):
        aaa = sheet.row_values(i)
        shuju.append(aaa)
    return shuju





# print(test_数据())




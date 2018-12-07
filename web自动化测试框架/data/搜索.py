#!/usr/bin/env python
#! -*- encoding=utf -*-
import xlrd

def test_数据():
    shuju = []
    f = xlrd.open_workbook('搜索.xls')
    sheet = f.sheets()[0]
    num = sheet.nrows
    for i in range(num):
        aaa = sheet.row_values(i)
        shuju.append(aaa)
    return shuju


print(test_数据())

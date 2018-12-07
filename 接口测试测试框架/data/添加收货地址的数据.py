#!/usr/bin/env python
# -*- coding=utf-8 -*-
import xlrd



def 数据():
    shuju = []
    f = xlrd.open_workbook('常用收货地址.xls')
    sheet = f.sheets()[0]
    num = sheet.nrows
    for i in range(1,num):
        aaa = sheet.row_values(i)
        shuju.append(aaa)
    return shuju
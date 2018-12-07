#!/user/bin/python
#-*- coding:utf-8 -*-
#Author:一土小亘兄
#@Time: 16:32

import xlrd



def create(row):
    f=xlrd.open_workbook('pppoe.xls')
    sheet=f.sheets()[0]
    a=sheet.row_values(row)
    print(a)
    return a

#
# for i in range(10):
#
#     w=create(i)
#     print(type(w[3]))
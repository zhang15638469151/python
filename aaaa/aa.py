#!/usr/bin/evn  python
# # -*- coding:utf-8 -*-
# def zhishu():
#     s=0
#     a=0
#     for i in range(2,101):
#         for j in range(2,i+1):
#             a=i%j
#             if a==0:
#                 break
#         if j==i:
#             s=s+i
#     return s
# # print(__name__)
# #
# # if __name__=='__main__':
# print(zhishu())
# #     print('hi')







#
#
# import os
# def w(a):
#     import os
#     with open(r'C:\Users\zhang\Desktop\a\aaaa\{}'.format(a),r,encoding='utf-8') as f:
#         b=f.readlines()
#         for i in b:
#             if i=='\n':
#                 b.remove(i)
#                 print(len(b))
#
#
# w(2)

















import xlrd
f = xlrd.open_workbook('text.xls')
sheet = f.sheets()[0]
for i in range(13,21):
    a = sheet.row_values(i)
    print(a)



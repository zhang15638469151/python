#！/usr/bin/env python
#-*- encoding=utf-8 -*-
#txt
#创建一个目录，创建十个文件，添加十行内容
# import os
# os.chdir(r'C:\Users\zhang\Desktop')
# os.mkdir(r'C:\Users\zhang\Desktop\目录')
# for i in range(10):
#     with open(r'C:\Users\zhang\Desktop\目录\{}.txt'.format(i),'a',encoding='utf-8') as f:
#         for j in range(10):
#             f.write('asdfghjkl'+'\n')
#
# with open('1.txt','w',encoding='utf-8') as f:
#     f.write('姓名，年龄，学号'+'\n')
#     for i in range(30):
#         f.write('张,20,2018'+'\n')





#Excel
#创建Excel表并添加数据
# import xlwt
# f = xlwt.Workbook()
# sheet = f.add_sheet('数据')
# sheet.write(0,0,'姓名')
# sheet.write(0,1,'年龄')
# sheet.write(0,2,'学号')
# for i in range(30):
#     sheet.write(i+1,0,'张')
#     sheet.write(i+1,1,20+1)
#     sheet.write(i+1,2,2018)
# f.save('text.xls')



#数据库
# import pymysql
# aaa = pymysql.connect(host='192.168.0.76',
#                       user='root',
#                       port=3306,
#                       password='654321',
#                       charset='utf8')
# #
# a = aaa.cursor()
# # a.execute('create database shujuku;')
# a.execute('use shujuku;')
# a.execute('create table biao(name char(255),age int,number int);')
# b = ['张',20,1]
# for i in range(20):
#     a.execute('insert into biao values("{}","{}","{}");'.format(b[0],b[1],b[2]+i))
#     aaa.commit()
# a.execute('select * from biao;')
# for j in a.fetchall():
#     print(j)




#txt到Excel
# import xlwt
# f=xlwt.Workbook()
# sheet = f.add_sheet('学生表')
# with open('1.txt','r',encoding='utf-8') as b:
#     a=b.readlines()
#     sheet.write(0,0,'姓名')
#     sheet.write(0,1,'年龄')
#     sheet.write(0,2,'学号')
#     for i in range(len(a)):
#         j = a[i].split(',')
#         print(j)
#         sheet.write(i+1,0,j[0])
#         sheet.write(i+1,1,j[1])
#         sheet.write(i+1,2,j[2].strip())
# f.save('text1.xls')




#txt到数据库
# import pymysql
# aaa = pymysql.connect(host='192.168.0.76',
#                       port=3306,
#                       user='root',
#                       password='654321',
#                       charset='utf8')
# a=aaa.cursor()
# a.execute('use shujuku;')
# with open('1.txt','r',encoding='utf-8') as f:
#     b = f.readlines()
#     # a.execute('create table biao1(姓名 char(255),年龄 int,学号 int);')
#     for i in b:
#         if i[0]!='姓名':
#             a.execute('insert into biao1 values("{}","{}","{}");').format(i[0],i[1],i[2])
# a.execute('select * from biao1;')
# for i in a.fetchall():
#     print(i)


#Excel到txt
# import xlrd
# f = xlrd.open_workbook('text1.xls')
# sheet = f.sheets()[0]
# a = sheet.row_values(0)
# b = sheet.nrows
# with open('2.txt','w',encoding='utf-8') as c:
#     c.write('{},{},{}'.format(a[0],a[1],a[2]))
#     for i in range(1,b):
#         d = sheet.row_values(i)
#         c.write('{},{},{}'.format(d[0],d[1],d[2])+'\n')


# 数据库到txt
# import pymysql
# aaa = pymysql.connect(host='192.168.0.70',
#                       port=3306,
#                       user='root',
#                       password='123456',
#                       charset='utf8')
# a = aaa.cursor()
# # a.execute('create database text1;')
# a.execute('use text1;')
# a.execute('desc biao;')
# b = a.fetchall()
# a.execute('select * from biao;')
# c = a.fetchall()
# with open('3.txt','w',encoding='utf-8') as f:
#     f.write('{},{},{}'.format(b[0][0],b[1][0],b[2][0])+'\n')
#     for i in range(1,len(c)):
#         f.write('{},{},{}'.format(c[i][0],c[i][1],c[i][2])+'\n')






#Excel到数据库
# import pymysql
# aaa = pymysql.connect(host='192.168.0.184',
#                       port=3306,
#                       user='root',
#                       password='123456',
#                       charset='utf8')
# import xlrd
# f = xlrd.open_workbook('text.xls')
sheet = f.sheets()[0]
a = sheet.row_values(0)
b = sheet.nrows
c = aaa.cursor()
c.execute('use text1;')
c.execute('create table biao1(姓名 char(255),年龄 int,学号 int);')
for i in range(1,b):
    a = sheet.row_values(i)
    c.execute('insert into biao values("{}","{}","{}");'.format(a[0],a[1]+1,a[2]))
    aaa.commit()
c.execute('select * from biao;')
for i in c.fetchall():
    print(i)





#数据库到Excel
# import xlwt
# import pymysql
# aaa = pymysql.connect(host='192.168.0.184',
#                       port=3306,
#                       user='root',
#                       password='123456',
#                       charset='utf8')
# a = aaa.cursor()
# a.execute('use text1;')
# a.execute('select * from biao;')
# b = a.fetchall()
# a.execute('desc biao;')
# c = a.fetchall()
# f = xlwt.Workbook()
# sheet = f.add_sheet('学生表')
# sheet.write(0,0,'c[0][0]')
# sheet.write(0,1,'c[1][0]')
# sheet.write(0,2,'c[2][0]')
# for i in b:
#     sheet.write(i,0,b[i][0])
#     sheet.write(i,1,b[i][1])
#     sheet.write(i,2,b[i][2])
#     f.save('text2.xls')


















# 1，把字符串变成整数
# a='33333322342'
# b=a[::-1]
# s=0
# for i,j in enumerate(b):
#     for h in range(10):
#         if str(h)==j:
#             s+=h*10**i
# print(s)




# 5、九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print()






#7、质数之和
# def zhishu(a,b):
#     s=0
#     c=0
#     for i in range(a,b+1):
#         for j in range(2,i+1):
#             c=i%j
#             if c==0:
#                 break
#         if j==i:
#                s=s+i
#     print(s)
#
# zhishu(10,100)





#创建一个目录，创建十个文件，添加十行内容
# import os
# os.chdir(r'C:\Users\zhang\Desktop')
# os.mkdir(r'C:\Users\zhang\Desktop\目录')
# for i in range(10):
#     with open(r'C:\Users\zhang\Desktop\目录\{}.txt'.format(i),'a',encoding='utf-8') as f:
#         for j in range(10):
#             f.write('asdfghjkl'+'\n')
# for m in range(10):
#     os.remove(r'C:\Users\zhang\Desktop\目录\{}.txt'.format(m))
# os.rmdir(r'C:\Users\zhang\Desktop\目录')



#txt到数据库
# import pymysql
# aaa = pymysql.connect(host='192.168.0.76',
#                       port=3306,
#                       user='root',
#                       password='654321',
#                       charset='utf8')
# a=aaa.cursor()
# a.execute('use shujuku;')
# with open('1.txt','r',encoding='utf-8') as f:
#     b = f.readlines()
#     # a.execute('create table biao1(姓名 char(255),年龄 int,学号 int);')
#     for i in b:
#         if i[0]!='姓名':
#             a.execute('insert into biao1 values("{}","{}","{}");').format(i[0],i[1],i[2])
# a.execute('select * from biao1;')
# for i in a.fetchall():
#     print(i)





#爬虫
# import re
# import requests
# class qiushi(object):
#     def qingqiu(self,page):
#         url = 'https://www.qiushibaike.com/8hr/page/{}/'.format(page)
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
#         response = requests.get(url=url,headers=head)
#         html = response.content.decode('utf-8')
#         return html
#
#     def guolv(self,abc):
#         shuju=[]
#         patt = re.compile('<div class="content"> (.*?) </div>',re.S)
#         items = patt.findall(abc)
#         for i in items:
#             i=i.replace('<span>','')
#             i=i.replace('</span>','')  
#             i=i.strip()
#             shuju.append(i)
#         return shuju
#
#
#     def save(self,shuju):
#         with open('a.txt','a',encoding='utf-8') as f:
#             for i in shuju:
#                 f.write(i+'\n')



# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host = ('192.168.0.68',2000)
# s.bind(host)
# s.listen(3)
# while True:
#     a,b=s.accept()
#     msg = a.recv(1024)
#     print(msg.decode('utf-8'))
#     reg = 'welcome'
#     a.send(reg.encode('utf-8'))
#
#
#
# import socket
# soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# soc.connect(('192.168.0.68',2000))
# aaa = 'hi'
# soc.send(aaa.encode('utf-8'))
# msg = soc.recv(1024)
# print(msg.decode('utf-8'))
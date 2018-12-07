# import random
# a=random.randrange(1,10)  #从1-10中间随机选取一个数
# # b=int(input('请输入一个数'))
# for i in range(3):
#     b = int(input('请输入一个数'))
#     if b<a:
#          print('小了')
#     elif b>a:
#          print('大了')
#     elif b==a:
#          print('正确')
#          break
# else:
#      print('笨蛋')
#质数之和
# a=int(input('请输入一个数'))
# s=0
# a=0
# for i in range(2,101):
#     for j in range(2,i+1):
#         a=i%j
#         if a==0:
#             break
#     if j==i:
#            s=s+i
# print(s)
#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print()
#
# a=[1,2,43,4,65,6,7,4,3,2,2]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# # print(b)
#
# for i in range(len(b)):
#     for j in range(len(b)-1):
#         if b[j] > b[j+1]:
#             t=b[j]
#             b[j]=b[j+1]
#             b[j+1]=t
# print(b)
#
# # print(b)
#
# # a=input('请输入一组数')
# # a=list(a)
# # a[0]=int(a[0])
# # a[1]=int(a[1])
# # a[2]=int(a[2])
# # a.sort()
# # if a[0]+a[1]>a[2]:
# #     if a[0]**2+a[1]**2==a[2]**2:
# #          print('直角三角形')
# #     elif a[0]**2+a[1]**2<a[2]**2:
# #          print('钝角三角形')
# #     elif a[0]**2+a[1]**2>a[2]**2:
# #          print('锐角三角形')
# # else:
# #     print('不能组成三角形')
#
# a='abccba'
# b=len(a)//2
# # c=0
# for c in range(b):
#     if a[c] !=a[-c-1]:
#         print('此字符串不回文')
#         break
# else:
#     print('此字符串回文')




#
#
#
#
#
#
#
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #创建socket
# host = ('192.168.0.62',5555)
# s.bind(host)
# s.listen(3)
# while True:
#     a,b = s.accept()
#     msg = a.recv(1024)
#     print(msg.decode('utf-8'))
#     reg = 'welcome'
#     a.send(reg.encode('utf-8'))
#
#
#
#
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host = ('192.168.0.62',5555)
# s.bind(host)
# s.listen(3)
# while True:
#     a,b = s.accept()
#     msg = a.recv(1024)
#     print(msg.decode('utf-8'))
#     reg = 'welcome'
#     a.send(reg.encode('utf-8'))
#
#
# import socket
# soc = socket.soctet(socket.AF_INET,socket.SOCK_STREAM)
# soc.connect(('192.168.0.62,555'))
# aaa = 'hi'
# soc.send(aaa.encode('utf-8'))
# msg = soc.recv(1024)
# print(msg.decode('utf-8'))





# import json
# date = {'name':'zhang','age':'20'}         #python中的字典
# date1 = json.dumps(date)                   #将Python中字典更改为json字符串（数据）
# # print(type(date1))                         #打印结果为字符串
# # print(date1)
# date2 = json.loads(date1)                #将json数据更改为字典
# print(date2)                             #打印结果为字典
# print(type(date2))                       #数据类型为字典









# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host = ('192.168.0.62',3000)
# s.bind(host)
# s.listen(3)
# while True:
#     a,b=s.accept()
#     msg = a.recv(1024)
#     print(msg.decode('utf-8'))
#     reg = 'welcome'
#     s.send(reg.encode('utf-8'))
#
#
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host = ('192.168.0.62',3000)
# s.bind(host)
# s.listen(3)
# while True:
#     a,b = s.accept()
#     msg = a.recv(1024)
#     print(msg.decode('utf-8'))
#     reg = 'welcome'
#     s.send(reg.encode('utf-8'))







# s = 0
# for i in range(2,101):
#     for j in range(2,i+1):
#         a = i%j
#         if a==0:
#             break
#     if i==j:
#         s+=i
# print(s)



# a='asdfghj'
# b = len(a)//2
# c=0
# for c in range(b):
#     if a[c] != a[-c-1]:
#         print('no')
#     else:
#         print('yes')

a = 'asdfdsa'
b = len(a)//2
c=0
for i in range(b):
    if a[c] != a[-c-1]:
        print('')

#
#
# import os
# os.chdir(r'C:/Users/zhang/Desktop')
# for i in os.chdir():
# #     if os.path.isdir(i):
# #
#
# import xlwt
# f=xlwt.Workbook()
# sheet=f.add_sheet('xueshengbiao')
# sheet.write(0,0,'neirong')
# f.save()
#
#
# import xlrd
# f=xlrd.open_workbook('text.xls')
# sheet=f.sheets()[0]
# a=sheet.nrows
# b = sheet.row_values(0)





#
# class Zhi():
#     def zhishu(self,a,b):
#         s=0
#         for i in range(a,b):
#             for j in range(2,i+1):
#                 c=i%j
#                 if c==0:
#                     break
#             if i==j:
#                 s+=i
#         print(s)
#
#
#
#
#
# class Jie(Zhi):
#     def jiecheng(self,a):
#         n=1
#         s=0
#         for i in range(1,a+1):
#             n=n*i
#             s=s+n
#         print(s)
#
#
# if __name__=='__main__':
#     print('hi')
#     print(Jie(5))






a='1234'
b=a[::-1]
c=0
for i,j in enumerate(b):
    for h in range(10):
        if str(h)==j:
            c+= h * 10 ** i
print(c)







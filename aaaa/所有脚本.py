# !/usr/bin/env python
# -*- coding:UTF-8 -*-
# 1，把字符串变成整数
# a='33333322342'
# b=a[::-1]
# s=0
# for i,j in enumerate(b):
#     for h in range(10):
#         if str(h)==j:
#             s+=h*10**i
# print(s)





# def shu(x):
#     a=x
#     b=x[::-1]
#     c=0
#     for i,j in enumerate(b):
#         for h in range(10):
#             if str(j)==h:
#                 c+=h*10**i
#     print(c)
# def zhuan(x):
#     a=x
#     b=a[::-1]
#     s=0
#     for i,j in enumerate(b):
#         for h in range(10):
#             if str(h)==j:
#                 s+=h*10**i
# #     print(s)
# # zhuan('1232143')



#2，十进制专十六进制
# a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# b=3242543
# c=''
# while True:
#     d=b%16
#     b=b//16
#     c+=a[d]
#     if b==0:
#         break
# print(c[::-1])



# def h(x):
#     a=['0','1','2','3','4','5','6','7','8','9','a','b','c','e','f','d']
#     b=x
#     c=''
#     while True:
#         d=b%16
#         b=b//16
#         c+=a[d]
#         if b==0:
#             break
#     print(c[::-1])
# h(271643)



# a = ['0','1']
# b = 123
# c = ''
# while True:
#     d=b%2
#     b=b//2
#     c+=a[d]
#     if b==0:
#         break
# print(c[::-1])




# 3，回文字符串
# a='111111'
# b=len(a)//2
# # c=0
# for c in range(b):
#     if a[c] !=a[-c-1]:
#         print('此字符串不回文')
#         break
# else:
#     print('此字符串回文')
#
# a='asdffg'
# b = len(a)//2
# c=0
# for c in range(b):
#     if a[c] != a[-c-1]:
#         print('yes')
# else:
#     print()




# def huiwen(x):
#     a=x
#     b=len(a)//2
#     c=0
#     for c in range(b):
#         if a[c]!=a[-c-1]:
#             print('bu')
#             break
#         else:
#             print('hui')
# huiwen('')




##4，去重排序
# a=[1,2,43,4,65,6,7,4,3,2,2]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# for i in range(len(b)):
#     for j in range(len(b)-1):
#         if b[j] > b[j+1]:
#             t=b[j]
#             b[j]=b[j+1]
#             b[j+1]=t
# print(b)









# 5、九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print()



#6、判断三角形
# a=input('请输入一组数')
# a = a.split(',')
# a[0]=int(a[0])
# a[1]=int(a[1])
# a[2]=int(a[2])
# a.sort()
# if a[0]+a[1]>a[2]:
#     if a[0]**2+a[1]**2==a[2]**2:
#          print('直角三角形')
#     elif a[0]**2+a[1]**2<a[2]**2:
#          print('钝角三角形')
#     elif a[0]**2+a[1]**2>a[2]**2:
#          print('锐角三角形')
# else:
#     print('不能组成三角形')

#7、质数之和
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
#     print(s)

#8、三次猜数据
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
#9、打印列表中第一大和第二大的数
# a=[2,4,7,9,3,8,9,7,2,1]
# b=a.copy()
# c=[]
# for m in b:
#     if m not in c:
#         c.append(m)
# for i in range(len(c)):
#     for j in range(len(c)-1):
#         if c[j]>c[j+1]:
#             t=c[j]
#             c[j]=c[j+1]
#             c[j+1]=t
# # print(c[-1],c[-2])
# h=a.count(c[-1])
# f=a.count(c[-2])
# print(h*c[-1])
# print(f*c[-2])



# print(a)

#10、排序（选择、冒泡）
#选择
# a=[3,2,5,7,3]
# # for i in range(len(a)):
# #     for j in range(len(a)-1):
# #         if a[i] < a[j]:
# #             a[i],a[j]=a[j],a[i]
# # print(a)
# #冒泡
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[j] > a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)
#11、把最小放在第一位，把最大放在最后一位
# a=[3,1,2,3,2,3,5,6,78,99,4]
# b=a.index(max(a))
# c=a.index(min(a))
# a[b],a[-1]=a[-1],a[b]
# a[c],a[0]=a[0],a[c]
# print(a)

# 12、将列表中的数向左挪一位
# a=[1,22,3,4,0]
# for i in range(len(a)-1):
#     a[i],a[i+1]=a[i+1],a[i]
# print(a)


# 13、随机加入一个数加入正确的位置
# a=int(input('请输入数'))
# b=[1,2,4,8]
# for i in b:
#     if a > i:
#         b.append(a)
#         b.sort()
#         break
# print(b)

#14、阶乘之和
# a=int(input('请输入一个数'))
# n=1
# s=0
# for i in range(1,a+1):
#     n=n*i
#     s=s+n
# print(s)

#15，水仙花数
# for i in range(100,1000):
#     b=i//100
#     c=i//10%10
#     d=i%10
#     a=b**3+c**3+d**3
#     if i==a:
#         print(i)

#16、任意四个数组成不同的三位数
# c=[]
# a=[1,2,3,4]
# for i in a:
#     for j in a:
#         for m in a:
#             if i!=j and i!=m and j!=m:
#                 b=i*100+j*10+m
#                 if b not in c:
#                     c.append(b)
# print(c)

#17、一个数个因数之和等于它本身
# for i in range(1,1001):
#     b=0
#     for j in range(1,i):
#         a=i%j
#         if a==0:
#             b=j+b
#     if b==i:
#         print(i)


#用while语句写十七个脚本
# a=1
# while a < 10:
#     b=1
#     while b<=a:
#         print('{}*{}={}'.format(a,b,a*b),end='\t')
#         b+=1
#     print()
#     a+=1
#
# def jiu():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print('{}*{}={}'.format(i,j,i*j),end='\t')
#         print()
# jiu()


# sum=[]
# a=[1,2,3,4]
# for i in a:
#     for j in a:
#         for n in a:
#             if i!=j and j!=n and n!=i:
#                 num=i*100+j*10+n
#                 if num not in sum:
#                     sum.append(num)
# print(sum)

#
# a=input('>')
# b=a.split(',')
# for i,j in enumerate(b):
#     b[i]=int(j)
#
# f=b.copy()
# c=max(b)
# for d in f:
#     if d==c:
#         print(d)
# for i in f:
#     if i==c:
#         f.remove(c)
# f.remove(c)
# c=max(f)
# for e in f:
#     if e==c:
#         print(e)
# import json
#
# a = {'asd':123}    # json字符串
#
# b = json.loads(a)
#
# print(b)



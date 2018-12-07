#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print()


#十六进制转十进制
# a = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# b = 12343
# c = ''
# while True:
#     d = b%16
#     b = b//16
#     c+=a[d]
#     if b==0:
#         break
# print(c[::-1])


#判断字符串是否回文
# a = 'asdfghgfdsa'
# b = len(a)//2
# for i in range(b):
#     if a[i] != a[-i-1]:
#         print('no')
#         break
# else:
#     print('yes')


#排序（冒泡和选择）
# a = [1,4,2,4,5]
# for i in a:
#     for j in range(len(a)-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)

# a = [3,2,1,4,3]
# for i in a:
#     for j in range(len(a)-1):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

#去重排序
# a = [1,2,3,1,1,2,3,4]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# for j in b:
#     for n in range(len(b)-1):
#         if b[n]>b[n+1]:
#             b[n],b[n-1]=b[n-1],b[n]
# print(b)


#质数之和
# s=0
# n=0
# for i in range(2,100):
#     for j in range(2,i+1):
#         n=i%j
#         if n==0:
#             break
#     if i==j:
#         s+=i
# print(s)


#阶乘之和
# s=0
# n=1
# for i in range(1,6):
#     n=n*i
#     s+=n
# print(s)


#水仙花数
# for i in range(100,1000):
#     a = i//100
#     b = i//10%10
#     c = i%10
#     d = a**3+b**3+c**3
#     if i==d:
#         print(i)



#1+2-3+4-5的值
# s = 0
# n = 0
# for i in range(2,100,2):
#     s+=i
# for j in range(1,100,2):
#     n+=j
# print(n-s)


#打印第一大和第二大的数
# a = [1,2,3,2,1,4,5,3,4]
# b = a.copy()
# c = []
# for i in b:
#     if i not in c:
#         c.append(i)
# for j in c:
#     for m in range(len(c)-1):
#         if c[m]>c[m+1]:
#             c[m],c[m+1]=c[m+1],c[m]
# print(c[-1],c[-2])
#
# a=20
# b=30
# s = 0
# for i in range(a, b+1):
#     for j in range(2, i + 1):
#         c = i % j
#         if c == 0:
#             break
#     if i == j:
#         s += i
# print(s)













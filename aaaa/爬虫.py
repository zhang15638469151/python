# import requests
# import re
# url = 'https://www.qiushibaike.com/text/'
# head = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
# response = requests.get(url=url,headers=head)
# html = response.content.decode('utf-8')
# patt = re.compile('<div class="content">(.*?)</span>',re.S)
# items = patt.findall(html)
# for i in items:
#     i=i.replace('<span>','')
#     i=i.replace(' ','')
#     with open('4.txt','a',encoding='utf-8') as f:
#         f.write(i+'\n')





# import requests
# import re
# url = 'http://www.doutula.com/article/detail/7181116'
# head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
# response = requests.get(url=url,headers=head)
# html = response.content.decode('utf-8')
# patt = re.compile('http://img.doutula.com/production/uploads/image/2018/11/06/(.*?).jpg|gif')
# items = patt.findall(html)
# for i in items:
#     print(i)


# import time
# print(time.time())
# print(time.localtime(124215435))
# print(time.strftime('%Y %m %d',time.localtime()))
# a = time.strptime('2018 11 8','%Y %m %d')
# print(a[0])










#
#
# a = '2018-11-08'
# b = a.split('-')
# c = time.strptime('{} {} {}'.format(b[0],b[1],b[2]),'%Y %m %d')
# if c[0]%100==0 and c[0]%400==0 or c[0]%4==0:
#     print('闰年')
# else:
#     print('no')


# a = '2018-11-08'
# b = a.split('-')
# c = time.strptime('{} {} {}'.format(b[0],b[1],b[2]),'%Y %m %d')
# print(time.mktime(c)-86400)





#
# import smtplib
# import email.mime.text
# import email.mime.multipart
# sender = '15638469151@163.com'
# recver = '15837806865@163.com'
# server = 'smtp.163.com'
# passwd = 'zt15638469151'
# message = email.mime.multipart.MIMEMultipart()
# message['from']=sender
# message['to']=recver
# message['subject']='zhuti'
# text = """youjianneirong"""
# text = email.mime.text.MIMEText(text)
# message.attach(text)
# smtp123 = smtplib.SMTP_SSL(server,465)
# smtp123.login(sender,passwd)
# smtp123.sendmail(sender,recver,message.as_string())
# smtp123.close()




#
#
# import requests
# import re
# import os
# class doutu():
#     def qingiu(self,page):
#         url = 'https://www.doutula.com/article/list/?page={}'.format(page)
#         head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
#         response = requests.get(url=url,headers=head)
#         html = response.content.decode('UTF-8')
#         return html
#
#     def guolv(self,zu):
#         ite = []
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
#         patt = re.compile('https://www.doutula.com/article/detail/[0-9]{7}')
#         patt1 = re.compile('<div class="random_title">(.*?)</div></div>')
#         items = patt.findall(zu)
#         items1 = patt.findall(zu)
#         for i in items1:
#             i=i.replace('<div class="date">2018-11-02','')
#             i = i.replace('<div class="date">2018-11-01','')
#             i = i.replace('<div class="date">2018-10-31','')
#             i = i.replace('<div class="date">2018-10-30','')
#             i = i.replace('<div class="date">2018-10-29','')
#             i = i.replace('<div class="date">2018-10-28','')
#             i = i.replace('<div class="date">2018-10-26', '')
#             i = i.replace('<div class="date">2018-10-27', '')
#             ite.append(i)
#         for m,n in enumerate(items):
#             os.mkdir(ite[m])
#             response=requests.get(url=n,headers=head)
#             html1 = response.content.decode('UTF-8')
#             patt2 = re.compile('onerror="this.src=(.*?).jpg|gif"')
#             items2 = patt2.findall(html1)
#             for a,b in items2:
#                 if a==
#                 print(j)
#
#
#
#
#
# a = doutu()
# zu = a.qingiu(2)
# a.guolv(zu)




#
# import requests
# import re
# import os
# ite=[]
# url = 'https://www.doutula.com/article/list/?page=2'
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
# response = requests.get(url=url,headers=head)
# html = response.content.decode('UTF-8')
# # print(html)
# patt = re.compile('https://www.doutula.com/article/detail/[0-9]{7}')
# patt1 = re.compile('<div class="random_title">(.*?)</div></div>')
# items = patt.findall(html)
# items1 = patt1.findall(html)
# # print(items1)
# for i in items1:
#     i=i.replace('<div class="date">2018-11-02','')
#     i = i.replace('<div class="date">2018-11-01','')
#     i = i.replace('<div class="date">2018-10-31','')
#     i = i.replace('<div class="date">2018-10-30','')
#     i = i.replace('<div class="date">2018-10-29','')
#     i = i.replace('<div class="date">2018-10-28','')
#     i = i.replace('<div class="date">2018-10-26', '')
#     i = i.replace('<div class="date">2018-10-27', '')
#     ite.append(i)
#     print(i)
#
#
# for i,j in enumerate(items):
#     os.mkdir(ite[i])
#     response=requests.get(url=j,headers=head)
#     html1 = response.content.decode('UTF-8')
#     patt2 = re.compile('onerror="this.src=(.*?).jpg|gif"')
#     items2 = patt2.findall(html1)
#     # print(items2)
#     for k,n in enumerate(items2):
#         n=n.replace("''",'')
#         n=n.replace('[]','')
#         if k==3 or k==8 or k==10:
#             n=n+'.gif'
#         else:
#             n=n+'.jpg'
#             n = n.replace("'",'')
#             tupian = requests.get(n)
#             print(n)
#             res1 = tupian.content
#             with open(r'{}\{}.jpg'.format(ite[i],k),'wb') as f:
#                 f.write(res1)












# import requests
# import re
# import os
# a=0
# url = 'https://www.doutula.com/article/list/?page=3'
# head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
# response = requests.get(url=url,headers=head)
# html = response.content.decode('UTF-8')
# patt = re.compile('https://www.doutula.com/article/detail/[0-9]{7}')
# items = patt.findall(html)
# name=re.compile('')
# for i in items:
#     response=requests.get(url=i,headers=head)
#     html1=response.content.decode('UTF-8')
#     patt1=re.compile(r'<img src="https://ws(.*?)" alt')
#     items1=patt1.findall(html1)
#     name=re.compile('<meta property="og:title" content="(.*?)" />')
#     name1=name.findall(html1)
#     print(name1)
#     os.mkdir(r'C:\Users\zhang\Desktop\a\{}'.format(name1[0]))
#     for j in items1:
#         j='https://ws'+j
#         re1=requests.get(j)
#         html2=re1.content
#         with open(r'C:\Users\zhang\Desktop\a\{}\{}.jpg'.format(name1[0],a),'wb') as f:
#             f.write(html2)
#         a+=1








import re
import requests
url = 'https://fe-api.zhaopin.com/c/i/sou?start=180&pageSize=60&cityId=538&industry=10100&salary=8001,10000&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=8001&_v=0.58147217&x-zp-page-request-id=3ca99bf1782a4ff4932a3f01cadf08d4-1542197930941-451599'
head = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
response = requests.get(url=url,headers=head)
html = response.content.decode('utf-8')
patt = re.compile('')
items = patt.findall(html)

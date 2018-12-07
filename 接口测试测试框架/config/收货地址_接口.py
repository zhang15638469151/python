#!/usr/bin/env python
# -*- coding=utf-8 -*-

import requests

class 添加收获_地址():

     def 收获_地址(self,*a):
         url = "http://www.zhaoapi.cn/user/addAddr"

         payload = 'uid="{}"&addr="{}"&mobile="{}"&name="{}"&token="{}"'.format(a[0], a[1].encode('utf-8'), a[2], a[3],
                                                                                a[4])
         headers = {
             'Content-Type': "application/x-www-form-urlencoded",
             'cache-control': "no-cache",
             'Postman-Token': "747e9598-96ec-40f5-9c4a-9140364f6574"
         }

         re = requests.request("POST", url, data=payload, headers=headers)
         b = re.text
         return b


# c = 添加收获_地址()
# print(c.收获_地址(22700,'北京市昌平区金域国际1-1-1',15837806865,15837806865,'B7674468CAC25325C13016653C09F3BD'))



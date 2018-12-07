#!/usr/bin/env python
# -*- coding=utf-8 -*-

import requests

class 地址_查询():

     def 常用地址(self,a):
         url = 'http://www.zhaoapi.cn/user/getAddrs'
         querystring = {'uid': "{}".format(a)}
         head = {
             'token': '6CE35A0F4F25A13F5E19357A0585A18F'}
         response = requests.get(url=url, headers=head, params=querystring)
         b = response.text
         return b




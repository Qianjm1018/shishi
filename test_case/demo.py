#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'qianjm'
__mtime__ = '2019/7/24'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
#发送请求，用到的数据
#安装或者引用
#使用别人写好的代码，首先要导包

#发送请求的包名，工具，框架-requests
#安装包
#导入
import requests

#发送post，json请求
# data={
#   "password": "123456",
#   "username": "admin"
# }
# q=requests.post("http://qa.yansl.com:8080/admin/login",json=data)
# print(q.text)

#发送post，键值对请求
# d={"adminId":22,"roleIds":[1,2]}
# c=requests.post("http://qa.yansl.com:8080/admin/role/update",data=d)
# print(c.text)

#发送get请求，键值对格式的数据
#get请求传数据，params
# param={"name":"admin","pageSize":5,"pageNum":1}
# req=requests.get("http://qa.yansl.com:8080/admin/list",params=param)
# print(req.text)

#{"orderSn":222,"receiverKeyword":222,"status":222,"orderType":222,"sourceType":222,"createTime":222,"pageSize":222,"pageNum":222}
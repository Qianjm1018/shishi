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
#发送一个post请求，请求正文格式为json

#请求方法

#url

#请求头中填写Content-Type: application/json

#请求正文中填写请求数据


from tools import request_tool
from tools import assert_tool
from tools import random_tool
from tools import mysql_tool
from tools import excel_tool
from tools import log_tool
from tools import os_tool
from tools import shell_tool
import pytest
import allure
# 项目根目录建config包，里面建conf.py文件，用于配置


# def test_login():
#     # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
#     url = 'http://qa.yansl.com:8080/admin/login'
#     req = {
#   "password": "123456",
#   "username": "admin"
# }
#     resp = request_tool.post_request(url,json=req)
#     #resp存的是当次请求中的所有回话信息
#     print(resp.text)
#
#     #resp.json()获取响应文中的所有内容，并且存入一个字典中
#     body = resp.json()
#     print(body)
    # 判断响应码
    # assert_tool.assert_equal(resp.status_code, 200)
    # # 自定义断言
    # assert_tool.assert_equal(body['code'],2000)
    # data =body['data']
    # if data !='':
    #     token = data['token']
    #     assert_tool.assert_not_null(token)

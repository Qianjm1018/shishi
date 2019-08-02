#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'qianjm'
__mtime__ = '2019/7/25'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓     ┏┓
            ┏┛┻━━━┛━━ ┻┓
            ┃      ☃   ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻   ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑  ┣┓
                ┃　永无BUG！┏┛
                ┗┓┓┏━┳┓┏┛ ━
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
#1、导包 demo_import
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
from config import conf
#2、找模版些测试用例 demo_http
#test_change_pwd_var方法名，可以自定义，但是必须以test_开头，test_user_registor
def test_user_regitor_1():
    #注册接口_全字段正常流
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    #url 网址.conf.GY_API_URL需要在config-conf.py文件中配置，相当于http请求默认值 '/admin/register'请求地址
    url = conf.GY_API_URL + '/admin/register'
    un="skc11"
    #请求数据，数据格式统一使用字典类型，注意json null对应字典中的none
    req = {
  "email": "296535@qq.com",
  "icon": "",
  "nickName": "skc",
  "note": "scn",
  "password": "123456",
  "username": un
}
    #post_request表示发送一个post请求，json=表示发送的数据格式为json 如果是数据是为键值对，用data=
    resp = request_tool.post_request(url, json=req)
    #resp.json()获取响应正文中的数据，并把这些数据从字符串转化为字典，如果想获取字符串格式数据，resp.text
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['data']["username"],un)

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
from config import conf


def test_change_pwd_var():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/admin/register'
    sn="qqqw"
    req = {
    "email": "5926261d@qq.com",
    "icon": "23",
    "nickName": "36",
    "note": "625",
    "password": "12356",
    "username": sn
    }

    resp = request_tool.post_request(url, json=req)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body["data"]["username"],sn)
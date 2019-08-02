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
data={}
un='digns'+random_tool.random_str_abc(5)
#注册
@allure.feature("后台用户管理流程")
@allure.story('注册-新用户')
def test_user_regitor():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/admin/register'
    random_tool.random_str_abc(5)
    un = 'digns' + random_tool.random_str_abc(5)
    req = {
  "password": "123456",
  "username": un
}

    resp = request_tool.post_request(url, json=req)
    body = resp.json()
    with allure.step("断言响应状态码，实际结果是：{}，预期结果为：200".format(resp.status_code)):
        pass
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    with allure.step("断言用户名，实际结果是：{}，预期结果为：{}".format(body["data"]["username"],un)):
        pass
    assert_tool.assert_equal(body["data"]["username"], un)
    data['id'] = body['data']['id']
    data['usename']=un
#给用户分配角色
@allure.feature("后台用户管理流程")
@allure.story('给用户分配角色：1，商品管理员。2，商品分类管理员。3、商品类型管理员。4、品牌管理员 ')
def test_user_admin_role():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL+'/admin/role/update'
    req = {
        "adminId": data['id'],
        "roleIds": [2]
    }

    resp = request_tool.post_request(url, data=req)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['data'],1)

#查询用户角色信息
@allure.feature("后台用户管理流程")
@allure.story('查询用户角色信息')
def test_admin_role():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL+'/admin/role/{}'.format(data['id'])

    resp = request_tool.get_request(url)
    body = resp.json()
    with allure.step("断言响应状态码，实际结果是：{}，预期结果为：200".format(resp.status_code)):
        pass
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    with allure.step("断言用户角色信息，实际结果是：{}，预期结果为：{}".format(body['data'][0]["name"],'商品')):
        pass
    assert_tool.assert_in(body['data'][0]["name"],'商品')

#登录
@allure.feature("后台用户管理流程")
@allure.story('登录')
def test_admin_login():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/admin/login'

    req = {

  "password": "123456",
  "username": data['usename']

    }

    resp = request_tool.post_request(url, json=req)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['data']["tokenHead"],"Bearer ")
    data["token"] = body['data']["tokenHead"] + body['data']["token"]

# #获取当前登录用户信息
@allure.feature("后台用户管理流程")
@allure.story('获取当前登录用户信息-根据token获取用户登录信息')
def test_admin_info():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/admin/info'
    headers = {
        'Authorization': data["token"],
        'charset': 'UTF-8'
    }
    resp = request_tool.get_request(url,headers=headers)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['data']["username"], data['usename'])


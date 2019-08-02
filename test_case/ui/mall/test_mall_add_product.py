#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'qianjm'
__mtime__ = '2019/7/31'
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
from time import sleep

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
@allure.feature("添加商品流程")
@allure.story("登录")

def test_login(base):
    #打开登录界面 http://qa.yansl.com/#/login
    base.get("打开登录界面","http://qa.yansl.com/#/login")
    #输入用户名//input[@name="username"]
    base.send_keys("输入用户名",'''//input[@name="username"]''','admin')
    #输入密码//input[@type="password"]
    base.send_keys("输入密码", '''//input[@type="password"]''','123456')
    #点击登录//span[contains(text(),'登录')]
    base.click('点击登录','''//span[contains(text(),'登录')]''')
    try:
        #残忍拒绝//span[text()='残忍拒绝']
        base.click('残忍拒绝','''//span[text()='残忍拒绝']''')
        # 点击登录//span[contains(text(),'登录')]
        base.click('点击登录', '''//span[contains(text(),'登录')]''')
    except:
        pass
    #添加一个断言 页面跳转至首页
    # f = False
    # try:
    #     base.local_element('//span[text()="首页"]')
    #     f= True
    # except:
    #     pass
    # assert_tool.assert_equal(f,True)
    sleep(2)
    ds = base.driver.page_source
    assert_tool.assert_in(ds,'首页')
    with allure.step("断言登录页面成功跳转"):
        allure.attach(ds,"实际结果",allure.attachment_type.TEXT)
        allure.attach('首页', "预期结果", allure.attachment_type.TEXT)
@allure.feature("添加商品流程")
@allure.story("打开添加商品页面")

def test_open_add(base):
    #点击//div[@class="hamburger-container"]
    #base.click('点击','''//div[@class="hamburger-container"]''')
    #点击商品(//span[@slot="title"])[1]
    base.click('点击商品', '''(//span[@slot="title"])[1]''')
    #点击商品分类//span[contains(text(),'添加商品')]
    base.click('点击商品分类', '''//span[contains(text(),'添加商品')]''')
    #添加断言，跳转至添加商品页面
    # f = False
    # try:
    #     base.local_element('''(//span[text()="添加商品"])[2]''')
    #     f = True
    # except:
    #     pass
    # assert_tool.assert_equal(f, True)
    #获取页面源代码
    sleep(2)
    page_soure = base.driver.page_source
    assert_tool.assert_in(page_soure,"添加商品")
    with allure.step("断言添加商品"):
        allure.attach(page_soure,"实际结果",allure.attachment_type.TEXT)
        allure.attach("添加商品", "预期结果", allure.attachment_type.TEXT)


@allure.feature("添加商品流程")
@allure.story("输入添加商品信息")
def test_add_category(base):
    #选择商品分类//li[contains(text(),"外套")]
    base.click('选择商品分类','//span[@class="el-cascader__label"]')
    #选择服装//li[contains(text(),"服装")]
    base.click('选择服装', '//li[contains(text(),"服装")]')
    #选择外套//li[contains(text(),"外套")]
    base.click('选择外套', '//li[contains(text(),"外套")]')
    #输入商品名称(//input[@type="text"])[2]
    base.send_keys('输入商品名称','(//input[@type="text"])[2]','卫衣')
    #输入副标题(//input[@type="text"])[3]
    base.send_keys('输入副标题', '(//input[@type="text"])[3]', '薄卫衣')
    #选择商品品牌//input[@placeholder="请选择品牌"]
    base.click('选择商品品牌', '//input[@placeholder="请选择品牌"]')
    #选择商品品牌小米//span[text()="小米"]
    base.click('选择商品品牌', '//span[text()="小米"]')
    #选择下一步(//button[@type="button"])[1]
    base.click('选择下一步', '(//button[@type="button"])[1]')
    #添加断言，跳转至下一页//label[contains(text(),"赠送积分")]
    # f=False
    # try:
    #     base.local_element('''//label[contains(text(),"赠送积分")]''')
    #     f= True
    # except:
    #     pass
    # assert_tool.assert_equal(f, True)
    sleep(2)
    soure = base.driver.page_source
    assert_tool.assert_in(soure,'赠送积分')
    with allure.step("断言赠送积分"):
        allure.attach(soure,"实际结果",allure.attachment_type.TEXT)
        allure.attach('赠送积分', "预期结果", allure.attachment_type.TEXT)
    base.click("下一步",'''(//button[@ type="button"])/span[text() = "下一步，填写商品属性"]''')
    # base.scroll_screen("滚动窗口")
    # #窗口切换至iframe
    # base.switch_to_frame("切入iframe","(//iframe)[1]")
    # #输入电脑端详情//body/p
    # base.send_keys("输入电脑端详情","//body",'测试')
    # #切除iframe
    # base.switch_to_content("切出iframe")
    base.click("下一步",'''(//button[@type="button"])/span[text()="下一步，选择商品关联"]''')
    base.click("下一步",'''(//button[@type="button"])/span[text()="完成，提交商品"]''')
    base.click("完成",'''//span[contains(text(),"确定")]''')
    sleep(5)
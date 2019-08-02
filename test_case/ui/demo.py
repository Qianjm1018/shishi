#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'qianjm'
__mtime__ = '2019/7/30'
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

from selenium import webdriver

from config.conf import DRIVER_PATH, GY_WEB_URL

#启动浏览器
driver = webdriver.Chrome(DRIVER_PATH)
#打开一个网址
driver.get(GY_WEB_URL)
#休眠几秒就是几
sleep(5)
#关闭浏览器
driver.quit()
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
#打开
driver = webdriver.Chrome(DRIVER_PATH)
#最大化浏览器（推荐使用）
driver.maximize_window()
#自定义浏览器大小（不推荐使用）
#driver.set_window_size(1280,960)
#打开网址
driver.get(GY_WEB_URL)
sleep(1)
driver.get('https://www.taobao.com')
sleep(1)
driver.get('https://www.jd.com')
#后退
driver.back()
sleep(1)
#前进
driver.forward()
sleep(1)
#刷新
driver.refresh()
sleep(0.5)

#关闭
#关闭浏览器
#driver.close()
#退出浏览器、驱动
driver.quit()

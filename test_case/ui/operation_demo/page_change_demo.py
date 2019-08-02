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

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from config.conf import DRIVER_PATH

driver = webdriver.Chrome(DRIVER_PATH)
driver.maximize_window()
def get_url():
    driver.get('D:\\softwaredata\\pycharm\\gy-api-qianjm\\demo.html')

def open_w():
    baidu = driver.find_element_by_partial_link_text('度娘')
    dd = driver.find_element_by_partial_link_text('当当')
    jd = driver.find_element_by_partial_link_text('京东')
    act = ActionChains(driver)
    act.key_down(Keys.CONTROL).click(baidu).click(dd).click(jd).key_up(Keys.CONTROL).perform()

def windows_change():
    #获取所有窗口的句柄
    handles = driver.window_handles
    #使用for循环根据窗口句柄来切换窗口
    for i in handles:
        driver.switch_to.window(i)
        #根据窗口的title来判断当前页面，如果包含我们想要的页面title，就停止循环break
        if(driver.title.__contains__('当当')):
           break
def reset_demo():
    driver.find_element_by_xpath('//input[@type="reset"]').click()

def alert_alert_demo():
    a = driver.switch_to.alert
    a.accept()

def submit_demo():
    driver.find_element_by_xpath('//input[@type="button"]').click()

def al_demo():
    ale = driver.switch_to.alert
    ale.send_keys('jidng')
    ale.dismiss()


if __name__ == '__main__':
    get_url()
    sleep(2)
    # open_w()
    # sleep(8)
    # windows_change()
    # sleep(2)
    # reset_demo()
    # sleep(2)
    # alert_alert_demo()
    # sleep(2)
    submit_demo()
    sleep(2)
    al_demo()
    sleep(4)
    driver.quit()
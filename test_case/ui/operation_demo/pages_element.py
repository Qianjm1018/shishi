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
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.select import Select

from config.conf import DRIVER_PATH

driver = webdriver.Chrome(DRIVER_PATH)
# 最大化浏览器（推荐使用）
driver.maximize_window()



def get_url(driver):
    driver.get('D:\\softwaredata\\pycharm\\gy-api-qianjm\\demo.html')

def  text_demo():

    #操作页面元素
    #定位元素
    text = driver.find_element_by_xpath('//input[@type="text"]')
    #清空元素中的内容
    text.clear()
    #在元素中输入内容
    text.send_keys('kid')
    #获取value属性的值






# def text():
#     driver = open_browser()
#     sleep(2)
#     driver.get('D:\\softwaredata\\pycharm\\gy-api-qianjm\\demo.html')
#     w = driver.find_element_by_xpath('//input[@type="text"]')
#     w.clear()
#     w.send_keys('1232.2')
#     print(w.get_attribute('value'))
#     sleep(2)
#     quit_browser(driver)
#
# if __name__ == '__main__':
#     text()


def  file_demo():

    #操作页面元素
    #定位元素
    file = driver.find_element_by_xpath('//input[@type="file"]')
    #清空元素中的内容
    file.clear()
    #在元素中输入内容
    file.send_keys('C:\\Users\\Administrator\\Desktop\\微信图片_20190327112457.png')

def radio_demo():
    radio = driver.find_element_by_xpath('//input[@type="radio"][1]')
    radio.click()

def checkbox_demo():
    check1 = driver.find_element_by_xpath('//input[@type="checkbox"][1]')
    check1.click()
    check2 = driver.find_element_by_xpath('//input[@type="checkbox"][2]')
    check2.click()
    check3 = driver.find_element_by_xpath('//input[@type="checkbox"][3]')
    check3.click()

def button_demo():
    button = driver.find_element_by_xpath('//input[@type="button"]')

    button.click()

def password_demo():
   password = driver.find_element_by_xpath('//input[@type="password"]')
   password.clear()
   password.send_keys('123654')

def number_demo():
   nm = driver.find_element_by_xpath('//input[@type="number"]')
   nm.clear()
   nm.send_keys('125')

def date_demo():
    js ='''var xpath = '//input[@type="date"]';var element = document.evaluate(xpath,document,null,XPathResult.ANY_TYPE,null).iterateNext();element.setAttribute("value","2019-07-30");'''
    driver.execute_script(js)
def time_demo():
    ti = '''var xpath = '//input[@type="time"]';var element = document.evaluate(xpath,document,null,XPathResult.ANY_TYPE,null).iterateNext();element.setAttribute("value","16:45");'''
    driver.execute_script(ti)

def textarea_demo():
   te = driver.find_element_by_xpath('//textarea')
   te.clear()
   te.send_keys('dagdasrteaw')

def select_demo():
    # select = driver.find_element_by_xpath('//option[@value="z2"]')
    # select.click()
    sel = driver.find_element_by_xpath('//select')
    select1 = Select(sel)
    select1.select_by_index(0)
    sleep(2)
    select1.select_by_value("z2")
    sleep(2)
    select1.select_by_visible_text('周龙3')
    sleep(2)

def chaolianjie_demo():
    #精确查询
    # clj = driver.find_elements_by_link_text('问问度娘')
    # clj.click()
    # driver.back()
    #模糊查询
    d= driver.find_element_by_partial_link_text("当")
    act = ActionChains(driver)
    # act.key_down(Keys.CONTROL).click(d).key_up(Keys.CONTROL).perform()
    # sleep(2)
    act.key_down(Keys.SHIFT).click(d).key_up(Keys.SHIFT).perform()
    sleep(2)
def submit_demo():
    submit = driver.find_element_by_xpath('//input[@type="submit"]')
    submit.click()

def reset_demo():
    reset = driver.find_element_by_xpath('//input[@type="reset"]')
    reset.click()

if __name__ == '__main__':
    get_url(driver)
    # sleep(2)
    # text_demo()
    # sleep(2)
    # file_demo()
    # sleep(2)
    # radio_demo()
    # sleep(2)
    # checkbox_demo()
    # sleep(2)
    # #button_demo()
    # # sleep(2)
    # password_demo()
    # sleep(2)
    # number_demo()
    # sleep(2)
    # date_demo()
    # sleep(2)
    # time_demo()
    # sleep(2)
    # textarea_demo()
    # sleep(2)
    # select_demo()

    chaolianjie_demo()
    sleep(2)

    # submit_demo()
    # sleep(2)
    reset_demo()
    sleep(2)
    driver.quit()











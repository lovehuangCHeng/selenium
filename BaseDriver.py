#coding=utf-8
import os
import time
from selenium import  webdriver
import configparser
import unittest
import json
import http.cookiejar
import urllib.request

class BascPage:

     '''
     构造方法，初始化driver 和 读取配置文件
     '''
     def __init__(self):
          chromedriver = "D:\python\python\chromedriver.exe"
          os.environ["webdriver.chrome.driver"] = chromedriver
          self.driver = webdriver.Chrome(chromedriver)
          self.config = configparser.ConfigParser()

     '''
          通过下面七种方法找元素的方法，并返回元素
     '''
     def get_element(self, key):
          self.config.read("../dataconfig/element.ini")
          vak = self.config.get("ZIP", key)
          by = vak.split("/")[0]
          by_value = vak.split("/")[1]
          try:
               if by == "id":
                    return self.driver.find_element_by_id(by_value)
               elif by == "name":
                    return self.driver.find_element_by_name(by_value)
               elif by == "className":
                    return self.driver.find_element_by_class_name(by_value)
               elif by == "cssSelector":
                    return self.driver.find_element_by_css_selector(by_value)
               elif by == "xpath":
                    return self.driver.find_element_by_xpath(by_value)
               elif by == "textLink":
                    return self.driver.find_element_by_link_text(by_value)
               elif by == "tagName":
                    return self.driver.find_element_by_tag_name(by_value)
          except Exception as e:
               print(e)
          return self.driver.find_element_by_xpath(by_value)

     '''
     输入框的输入方法，先清除输入框的内容，再输入值
     '''
     def sendkeys(self, key, value):
          element = self.get_element(key)
          time.sleep(1)
          element.clear()
          time.sleep(1)
          element.send_keys(value)
     '''
     点击的方法
     '''
     def click(self,key):
          element = self.get_element(key)
          element.click()
     '''
     定位下拉框，获取下拉框的的元素，通过index定位
     '''
     def selector(self, key, index):
          element = self.get_element(key)
          time.sleep(1)
          element.select_by_index(index)

     '''
     定义open url 的方法,打开浏览器
     '''
     def open(self, url):
          self.driver.get(url)
          time.sleep(1)
          self.driver.maximize_window()

     '''
     定义script方法，用于执行js脚本，范围执行结果
     '''
     def script(self, src):
          self.driver.execute_script(src)
     '''
     关闭浏览器
     '''
     def quet(self):
          self.driver.quit()
     '''
     设置cookie 的方法
     '''
     def setCookie(self,cookie_dict):
          self.driver.add_cookie(cookie_dict)

     '''
         删除cookie 的方法
     '''

     def delCookie(self):
          self.driver.delete_all_cookies()

     '''
          保存cookie到文件中
     '''
     def saveCookis(self):
          dict_cookies = {}
          for cookie in self.driver.get_cookies():
               dict_cookies[cookie['name']] = cookie['value']
               if cookie['name'] == "nova_pms_auth_Default":
                    with open('../dataconfig/cookies.txt', 'w') as f:
                         cook=json.dumps(cookie)
                         f.write(cook)
                         f.close()
     '''
     从文件中读取cookie
     '''
     def readCookie(self):
          #url="test.wuyezhijia.cn"
          with open('../dataconfig/cookies.txt', 'r', encoding='utf-8') as f:
               s=f.read()
               cookies = json.loads(s)
               print(cookies)
               self.driver.add_cookie(cookies)

     '''
     切换ifram 窗口
     '''
     def switch_fram(self,key):
          fram=self.get_element(key)
          time.sleep(2)
          self.driver.switch_to.frame(fram)
     '''
     断言的方法,通过元素的字符串判断是否有这个元素
     '''
     def assertTure(self,key,exceptasser):
          element=self.get_element(key).text
          time.sleep(2)
          if element.find(exceptasser):
               return  True
          else:
               return  False



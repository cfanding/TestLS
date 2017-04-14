# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import config
import os
import time
# 调用IE浏览器
# iedriver = "C:\Program Files\Internet Explorer\IEDriverServer.exe"
# os.environ["webdriver.ie.driver"] = iedriver
# browser = webdriver.Ie(iedriver)
# 调用Chrome浏览器
# Copyright DingYa
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver

browser = webdriver.Chrome(chromedriver)

def setUpModule():
    global browser


def tearDownModule():
    global browser
    browser.quit()


class LSTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = browser
        cls.browser.wait = WebDriverWait(cls.browser, 10)
        cls.browser.implicitly_wait(10)

    def login_into_page(self, url):
        self.browser.get(url)
        # 输入正确的用户名
        self.browser.find_element(By.ID, "username").clear()
        self.browser.find_element(By.ID, "username").send_keys(config.USERNAME)

        # 输入正确的密码
        self.browser.find_element(By.ID, 'password').clear()
        self.browser.find_element(By.ID, 'password').send_keys(config.PASSWORD)

        # 点击登录
        time.sleep(2)
        self.browser.find_element(By.XPATH, '//*[@id="login-main"]/div[2]/div[4]').click()

        # 验证当前网址和url是否一致
        # self.browser.wait.until(lambda _driver: _driver.current_url == url)
        self.browser.maximize_window()

    @staticmethod
    def random_string(name_length):
        """随机生成一个指定长度的字符串.

        :param name_length:(int) specify length
        :return:
        """
        return ''.join(random.sample(string.ascii_letters, name_length))

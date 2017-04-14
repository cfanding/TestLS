# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from selenium.webdriver.common.by import By
from utils import LSTest
import config


class Login(LSTest):
    u"""输入正确的用户名和密码能登陆成功"""

    def test_login_success(self):
        u"""输入正确的用户名和密码能登陆成功"""
        url = config.LOGIN_URL
        self.login_into_page(url)

        try:
            text = self.browser.find_element(By.ID, 'contact').text
            print text
            if u'监督电话' in text:
                print (u"登录成功")

        except Exception:
            print (u"登录失败")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Login("test_login_success"))

    results = unittest.TextTestRunner().run(suite)

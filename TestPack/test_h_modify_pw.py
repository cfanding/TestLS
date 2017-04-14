# -*- coding: utf-8 -*-
from __future__ import absolute_import
from selenium.webdriver.common.by import By
from utils import LSTest
from time import sleep
from TestPack.models import function
import unittest
import config


class ModifyPassword(LSTest):
    u"""修改密码校验"""
    def test_a_modify_password_rt(self):
        u"""修改正确密码"""
        # url = config.Modify_URL
        # # 修改密码
        # self.browser.get(url)
        url = config.LOGIN_URL
        self.login_into_page(url)

        sleep(2)
        # 个人中心
        personal_center_xpath = '/html/body/div/div[1]/div/ul[2]/div/span'
        self.browser.find_element(By.XPATH, personal_center_xpath).click()

        # 修改密码
        modify_xpath = '/html/body/div/div[1]/div/ul[2]/li[3]/div/span'
        self.browser.find_element(By.XPATH, modify_xpath).click()
        # 旧密码
        old_pw_xpath = '//*[@id="oldPwd"]'
        self.browser.find_element(By.XPATH, old_pw_xpath).clear()
        self.browser.find_element(By.XPATH, old_pw_xpath).send_keys(config.PASSWORD)
        # 新密码
        new_pw_xpath = '//*[@id="newPwd"]'
        self.browser.find_element(By.XPATH, new_pw_xpath).clear()
        self.browser.find_element(By.XPATH, new_pw_xpath).send_keys(config.CHANGEPW)
        # 确认密码
        confirm_pw_xpath = '//*[@id="confirmPwd"]'
        self.browser.find_element(By.XPATH, confirm_pw_xpath).clear()
        self.browser.find_element(By.XPATH, confirm_pw_xpath).send_keys(config.CHANGEPW)

        # 修改
        change_pw_xpath = '//*[@id="pwd-main"]/div/div[3]'
        self.browser.find_element(By.XPATH, change_pw_xpath).click()

        # 弹出框校验
        alert_xpath = '//*[@id="_modalContent"]/div'
        text = self.browser.find_element(By.XPATH, alert_xpath).text
        print (text)
        sleep(2)
        function.insert_img(self.browser, "user_pw_true.jpg")
        self.browser.refresh()

    def test_b_modify_password_ow(self):
        u"""原密码错误校验"""
        # 个人中心
        personal_center_xpath = '/html/body/div/div[1]/div/ul[2]/div/span'
        self.browser.find_element(By.XPATH, personal_center_xpath).click()
        # 修改密码
        modify_xpath = '/html/body/div/div[1]/div/ul[2]/li[3]/div/span'
        self.browser.find_element(By.XPATH, modify_xpath).click()
        # 旧密码
        old_pw_xpath = '//*[@id="oldPwd"]'
        self.browser.find_element(By.XPATH, old_pw_xpath).clear()
        self.browser.find_element(By.XPATH, old_pw_xpath).send_keys(config.PASSWORD)
        # 新密码
        new_pw_xpath = '//*[@id="newPwd"]'
        self.browser.find_element(By.XPATH, new_pw_xpath).clear()
        self.browser.find_element(By.XPATH, new_pw_xpath).send_keys(config.CHANGEPW)
        # 确认密码
        confirm_pw_xpath = '//*[@id="confirmPwd"]'
        self.browser.find_element(By.XPATH, confirm_pw_xpath).clear()
        self.browser.find_element(By.XPATH, confirm_pw_xpath).send_keys(config.CHANGEPW)

        # 修改
        change_pw_xpath = '//*[@id="pwd-main"]/div/div[3]'
        self.browser.find_element(By.XPATH, change_pw_xpath).click()

        # 弹出框校验
        alert_xpath = '//*[@id="_modalContent"]/div'
        text = self.browser.find_element(By.XPATH, alert_xpath).text
        print (text)
        sleep(2)
        function.insert_img(self.browser, "user_pw_ow.jpg")
        self.browser.refresh()
        sleep(5)

    def test_c_modify_password_d(self):
        u"""新密码两次输入不一致"""
        # 个人中心
        personal_center_xpath = '/html/body/div/div[1]/div/ul[2]/div/span'
        self.browser.find_element(By.XPATH, personal_center_xpath).click()
        # 修改密码
        modify_xpath = '/html/body/div/div[1]/div/ul[2]/li[3]/div/span'
        self.browser.find_element(By.XPATH, modify_xpath).click()
        # 旧密码
        old_pw_xpath = '//*[@id="oldPwd"]'
        self.browser.find_element(By.XPATH, old_pw_xpath).clear()
        self.browser.find_element(By.XPATH, old_pw_xpath).send_keys(config.CHANGEPW)
        # 新密码
        new_pw_xpath = '//*[@id="newPwd"]'
        self.browser.find_element(By.XPATH, new_pw_xpath).clear()
        self.browser.find_element(By.XPATH, new_pw_xpath).send_keys(config.NEWPW)
        # 确认密码
        confirm_pw_xpath = '//*[@id="confirmPwd"]'
        self.browser.find_element(By.XPATH, confirm_pw_xpath).clear()
        self.browser.find_element(By.XPATH, confirm_pw_xpath).send_keys(config.SHORTPW)

        # 修改
        change_pw_xpath = '//*[@id="pwd-main"]/div/div[3]'
        self.browser.find_element(By.XPATH, change_pw_xpath).click()

        # 弹出框校验
        alert_xpath = '//*[@id="_modalContent"]/div'
        text = self.browser.find_element(By.XPATH, alert_xpath).text
        print (text)
        sleep(2)
        function.insert_img(self.browser, "user_pw_d.jpg")
        self.browser.refresh()
        sleep(5)

    def test_d_modify_password_ce(self):
        u"""确认密码不可为空校验"""
        # 个人中心
        personal_center_xpath = '/html/body/div/div[1]/div/ul[2]/div/span'
        self.browser.find_element(By.XPATH, personal_center_xpath).click()
        # 修改密码
        modify_xpath = '/html/body/div/div[1]/div/ul[2]/li[3]/div/span'
        self.browser.find_element(By.XPATH, modify_xpath).click()
        # 旧密码
        old_pw_xpath = '//*[@id="oldPwd"]'
        self.browser.find_element(By.XPATH, old_pw_xpath).clear()
        self.browser.find_element(By.XPATH, old_pw_xpath).send_keys(config.CHANGEPW)
        # 新密码
        new_pw_xpath = '//*[@id="newPwd"]'
        self.browser.find_element(By.XPATH, new_pw_xpath).clear()
        self.browser.find_element(By.XPATH, new_pw_xpath).send_keys(config.NEWPW)
        # 确认密码
        confirm_pw_xpath = '//*[@id="confirmPwd"]'
        self.browser.find_element(By.XPATH, confirm_pw_xpath).clear()
        sleep(5)

        # 修改
        change_pw_xpath = '//*[@id="pwd-main"]/div/div[3]'
        self.browser.find_element(By.XPATH, change_pw_xpath).click()

        # 弹出框校验
        alert_xpath = '//*[@id="_modalContent"]/div'
        text = self.browser.find_element(By.XPATH, alert_xpath).text
        print (text)
        sleep(2)
        function.insert_img(self.browser, "user_pw_ce.jpg")
        self.browser.refresh()
        sleep(5)

    def test_e_modify_password_oe(self):
        u"""新密码不可为空校验"""
        # 个人中心
        personal_center_xpath = '/html/body/div/div[1]/div/ul[2]/div/span'
        self.browser.find_element(By.XPATH, personal_center_xpath).click()
        # 修改密码
        modify_xpath = '/html/body/div/div[1]/div/ul[2]/li[3]/div/span'
        self.browser.find_element(By.XPATH, modify_xpath).click()
        # 旧密码
        old_pw_xpath = '//*[@id="oldPwd"]'
        self.browser.find_element(By.XPATH, old_pw_xpath).clear()
        self.browser.find_element(By.XPATH, old_pw_xpath).send_keys(config.CHANGEPW)
        # 新密码
        new_pw_xpath = '//*[@id="newPwd"]'
        self.browser.find_element(By.XPATH, new_pw_xpath).clear()

        # 确认密码
        confirm_pw_xpath = '//*[@id="confirmPwd"]'
        self.browser.find_element(By.XPATH, confirm_pw_xpath).clear()
        self.browser.find_element(By.XPATH, confirm_pw_xpath).send_keys(config.NEWPW)

        # 修改
        change_pw_xpath = '//*[@id="pwd-main"]/div/div[3]'
        self.browser.find_element(By.XPATH, change_pw_xpath).click()

        # 弹出框校验
        alert_xpath = '//*[@id="_modalContent"]/div'
        text = self.browser.find_element(By.XPATH, alert_xpath).text
        print (text)
        sleep(2)
        function.insert_img(self.browser, "user_pw_oe.jpg")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ModifyPassword("test_a_modify_password_rt"))
    suite.addTest(ModifyPassword("test_b_modify_password_ow"))
    suite.addTest(ModifyPassword("test_c_modify_password_d"))
    suite.addTest(ModifyPassword("test_d_modify_password_ce"))
    suite.addTest(ModifyPassword("test_e_modify_password_oe"))

    results = unittest.TextTestRunner().run(suite)

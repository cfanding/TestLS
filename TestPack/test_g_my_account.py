# -*- coding: utf-8 -*-
from __future__ import absolute_import
from selenium.webdriver.common.by import By
from utils import LSTest
from time import sleep
import unittest
import config
import MySQLdb


class MyAccount(LSTest):
    u"""我的账户集成数据库校验"""
    def test_my_account(self):
        u"""我的账户集成数据库校验"""
        # url = config.MAccount_URL
        # # 我的账户
        # self.browser.get(url)
        # url = config.LOGIN_URL
        # self.login_into_page(url)

        sleep(5)
        self.browser.refresh()
        # 个人中心
        personal_center_xpath = '/html/body/div/div[1]/div/ul[2]/div/span'
        self.browser.find_element(By.XPATH, personal_center_xpath).click()
        # 我的账户
        my_account_xpath = '//*[@id="left"]/div/ul[2]/li[2]/div/span'
        self.browser.find_element(By.XPATH, my_account_xpath).click()
        sleep(5)
        # 公司名称
        company_name_xpath = '//*[@id="account-main"]/div/div[2]/div[1]/span[2]'
        company_name = self.browser.find_element(By.XPATH, company_name_xpath).text
        print (company_name)
        # 公司地址
        company_address_xpath = '//*[@id="account-main"]/div/div[2]/div[2]/span[2]'
        company_address = self.browser.find_element(By.XPATH, company_address_xpath).text
        print (company_address)

        # 联系电话
        company_tel_xpath = '//*[@id="account-main"]/div/div[2]/div[3]/span[2]'
        company_tel = self.browser.find_element(By.XPATH, company_tel_xpath).text
        print (company_tel)
        # 登录账号
        login_account_xpath = '//*[@id="account-main"]/div/div[2]/div[4]/span[2]'
        login_account = self.browser.find_element(By.XPATH, login_account_xpath).text
        print (login_account)
        # 当前套餐
        user_business_xpath = '//*[@id="account-main"]/div/div[2]/div[5]/span[2]'
        user_business = self.browser.find_element(By.XPATH, user_business_xpath).text
        print (user_business)
        # 套餐有效期
        start_end_xpath = '//*[@id="account-main"]/div/div[2]/div[6]/span[2]'
        start_end = self.browser.find_element(By.XPATH, start_end_xpath).text
        print (start_end)
        # 套餐余额
        account_balance_xpath = '//*[@id="account-main"]/div/div[2]/div[7]/span[2]'
        account_balance = self.browser.find_element(By.XPATH, account_balance_xpath).text
        accountB = account_balance.encode('gbk')
        Balance = int(filter(str.isdigit, accountB))
        print (Balance)

        DB_HOST = '192.168.57.167'
        DB_NAME = 'mea_video'
        DB_USER = 'root'
        DB_PASSWORD = 'ggcl1205'

        # 打开数据库连接
        conn = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME, port=3306, charset="utf8")

        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        # 使用execute方法执行SQL语句
        thirdid = config.USERNAME
        sql_user_id = "SELECT user_id FROM user_third where third_id = '%s'" % thirdid
        cursor.execute(sql_user_id)
        # 使用 fetchone() 方法获取一条数据库。
        results = cursor.fetchone()
        user_id = results[0]
        print (user_id)

        conn = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME, port=3306, charset="utf8")
        sql_my_account = "SELECT user.company_name,user.company_address,user.contact_telno,(SELECT business_package.name FROM business_package INNER JOIN user_account ON business_package.id = user_account.business_package_id WHERE user_account.user_id = '%s')as name,user_account.package_start_time,user_account.package_end_time,user_account.time_amount FROM user INNER JOIN user_account ON user.id = user_account.user_id WHERE user.id = '%s'" % (user_id, user_id)
        cursor = conn.cursor()
        cursor.execute(sql_my_account)
        results = cursor.fetchone()
        list = [results[0], results[1], results[2], results[3], results[4], results[5], results[6]]
        cursor.close()
        conn.close()
        for a in list:
            if a == results[0]:
                self.assertEqual(a, company_name)
                print (u"公司名称对比正确")
            elif a == results[1]:
                self.assertEqual(a, company_address)
                print (u"公司地址对比正确")
            elif a == results[2]:
                self.assertEqual(a, company_tel)
                print (u"联系电话对比正确")
            elif a == results[3]:
                self.assertEqual(a, user_business)
                print (u"当前套餐对比正确")
            elif a == results[4]:
                b = str(results[4])[0:10]
            elif a == results[5]:
                c = str(results[5])[0:10]
                timeright = b+' '+'-'+' '+c
                self.assertEqual(timeright, start_end)
                print (u"套餐有效期对比正确")
            else:
                self.assertEqual(a, Balance)
                print (u"套餐余额对比正确")
        print (u"我的账户集成数据库对比正确")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(MyAccount("test_my_account"))

    results = unittest.TextTestRunner().run(suite)

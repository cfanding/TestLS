# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from selenium.webdriver.common.by import By
from utils import LSTest
import config
from time import sleep
import MySQLdb


class AccountBalance(LSTest):
    u"""账户余额校验"""
    def test_account_balance(self):
        u"""账户余额集成数据库校验"""
        # url = config.LOGIN_URL
        # self.login_into_page(url)
        sleep(2)

        # 账户余额展示
        balance_xpath = '//*[@id="balance"]/div/span'
        countBa = self.browser.find_element(By.XPATH, balance_xpath).text
        print (countBa)

        DB_HOST = '192.168.57.167'
        DB_NAME = 'mea_video'
        DB_USER = 'root'
        DB_PASSWORD = 'ggcl1205'

        # 打开数据库连接
        conn = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME, port=3306, charset="utf8")

        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        thirdid = config.USERNAME
        print ("Login accout is %s" %thirdid)
        mystring = countBa
        mystring2 = mystring.encode('gbk')
        counts = int(filter(str.isdigit, mystring2))

        # 使用execute方法执行SQL语句
        sql_third_id = "SELECT * FROM user_third where third_id = '%s'" % thirdid
        cursor.execute(sql_third_id)
        # 使用 fetchone() 方法获取一条数据库。
        results = cursor.fetchone()
        user_id = results[1]
        print ("user id is %d" %user_id)

        conn = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME, port=3306, charset="utf8")
        sql_user_id = "SELECT * FROM user_account where user_id = '%s'" % user_id
        cursor = conn.cursor()
        cursor.execute(sql_user_id)
        results = cursor.fetchone()
        time_amount = results[8]
        cursor.close()
        conn.close()

        if time_amount == counts:
            print (u'前端显示的余额和数据库集成一致')


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(AccountBalance("test_account_balance"))

    results = unittest.TextTestRunner().run(suite)

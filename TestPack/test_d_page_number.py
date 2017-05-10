# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from selenium.webdriver.common.by import By
from utils import LSTest
import config
from time import sleep
import MySQLdb
import math


class PageNumber(LSTest):
    u"""分页数据"""
    def test_page_number(self):
        u"""共多少页"""
        # url = config.Templates_URL
        # # 模板商城
        # self.browser.get(url)
        # url = config.LOGIN_URL
        # self.login_into_page(url)

        self.browser.refresh()
        # 个人场景
        personal_xpath = '//*[@id="category-top"]/div[1]/span'
        self.browser.find_element(By.XPATH, personal_xpath).click()
        third_xpath = '//*[@id="tpl-container"]/div/div[1]/div[1]'
        self.browser.find_element(By.XPATH, third_xpath).click()
        sleep(1)

        DB_HOST = '192.168.57.167'
        DB_NAME = 'mea_video'
        DB_USER = 'root'
        DB_PASSWORD = 'ggcl1205'

        # 打开数据库连接
        conn = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME, port=3306, charset="utf8")

        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        page_nu_xpath = '//*[@id="info"]/span[2]'
        pagenu = self.browser.find_element(By.XPATH, page_nu_xpath).text
        print ("Page display pages is %s" % pagenu)
        PN = int(pagenu)
        third_xpath = '//*[@id="tpl-container"]/div/div[1]/div[1]'
        category = self.browser.find_element(By.XPATH, third_xpath).text
        print ("category is %s" % category)

        # 使用execute方法执行SQL语句
        category_name = category
        sql_category_id = "select * from category where name = '%s'" % category_name
        cursor.execute(sql_category_id)

        # 使用 fetchone() 方法获取一条数据库。
        results = cursor.fetchone()
        categoryid = results[0]
        print ("category id is %s" % categoryid)

        conn = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME, port=3306, charset="utf8")
        sql_counts = "select count(*) from (select * from video_template vep ) vp INNER JOIN (select * from category_and_template cg where cg.category_id = %s )as ctp on ctp.template_id = vp.id " % categoryid
        cursor = conn.cursor()
        cursor.execute(sql_counts)
        results = cursor.fetchone()
        counts = results[0]
        cursor.close()
        conn.close()
        print ("the sql counts is %s" % counts)
        pageNumber = (counts/12.00)
        print ("%f" % pageNumber)
        print ("Total pages is %s" % math.ceil(pageNumber))
        sqlcounts = int(math.ceil(pageNumber))

        if PN == sqlcounts:
            print (u"页面总页数和数据库集成校验一致")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(PageNumber("test_page_number"))

    results = unittest.TextTestRunner().run(suite)
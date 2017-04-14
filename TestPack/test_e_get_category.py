# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from selenium.webdriver.common.by import By
from utils import LSTest
from TestPack.models import function
import MySQLdb
import config


class GetCategory(LSTest):
    u"""获取栏目数"""
    def test_get_category(self):
        u"""获取栏目数集成数据库对比"""
        # url = config.Templates_URL
        # # 模板商城
        # self.browser.get(url)
        url = config.LOGIN_URL
        self.login_into_page(url)

        # 个人场景
        personal_xpath = '//*[@id="category-top"]/div[1]/span'
        personal = self.browser.find_element(By.XPATH, personal_xpath).text
        print (u"二级栏目名称是" + personal)

        DB_HOST = '192.168.57.167'
        DB_NAME = 'mea_video'
        DB_USER = 'root'
        DB_PASSWORD = 'ggcl1205'

        # 打开数据库连接
        conn = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME, port=3306, charset="utf8")

        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        # 使用execute方法执行SQL语句
        sql_category_id = "SELECT category.name FROM category where id in (SELECT category_relation.child_id FROM category_relation INNER JOIN category ON category_relation.parent_id = category.id WHERE category.name = '%s') ORDER BY category.order ASC" % personal
        cursor.execute(sql_category_id)
        # 使用 fetchall() 方法获取数据库。
        # cursor.scroll(0, "absolute")
        jsonDate = []
        for line in cursor.fetchall():
            jsonDate.append(line[0])
        print (jsonDate)[0]
        print (jsonDate)[1]
        print (jsonDate)[2]
        print (jsonDate)[3]
        # 栏目个数
        print len(jsonDate)
        cursor.close()
        conn.close()
        function.insert_img(self.browser, "category_number.jpg")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(GetCategory("test_get_category"))

    results = unittest.TextTestRunner().run(suite)
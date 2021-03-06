# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from selenium.webdriver.common.by import By
from utils import LSTest
from TestPack.models import function
from time import sleep
import MySQLdb
import json


class MyOrder (LSTest):
    u"""我的订单校验状态"""
    def test_custom_order(self):
        u"""提交定制化订单校验状态"""
        # url = config.Custom_URL
        # # 模板商城
        # self.browser.get(url)
        # url = config.LOGIN_URL
        # self.login_into_page(url)

        # 视频商城
        video_shop_xpath = '/html/body/div/div[1]/div/ul[1]/div/span'
        self.browser.find_element(By.XPATH, video_shop_xpath).click()
        sleep(5)
        # 我要定制
        dingzhi_xpath = '//*[@id="left"]/div/ul[1]/li[2]/div/span'
        self.browser.find_element(By.XPATH, dingzhi_xpath).click()
        second_xpath = '//*[@id="category-top"]/div[1]/span'
        self.browser.find_element(By.XPATH, second_xpath).click()
        sleep(2)
        dz_xpath = '//*[@id="data"]/div[1]/div[2]/div'
        self.browser.find_element(By.XPATH, dz_xpath).click()

        # 定制需求
        self.browser.find_element(By.NAME, 'company').clear()
        self.browser.find_element(By.NAME, 'company').send_keys(self.random_string(4))
        self.browser.find_element(By.NAME, 'contact').clear()
        self.browser.find_element(By.NAME, 'contact').send_keys(self.random_string(4))
        self.browser.find_element(By.NAME, 'mobile').clear()
        self.browser.find_element(By.NAME, 'mobile').send_keys("13652255262")

        # 确认需求
        confirm_xpath = '//*[@id="submit-custom-order"]/div[10]'
        self.browser.find_element(By.XPATH, confirm_xpath).click()

        DB_HOST = '192.168.57.167'
        DB_NAME = 'mea_video'
        DB_USER = 'root'
        DB_PASSWORD = 'ggcl1205'

        # 打开数据库连接
        conn = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME, port=3306, charset="utf8")

        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        orderId = '//*[@id="tpl-order"]/table/tbody/tr[2]/td[2]'
        orderNumber = self.browser.find_element(By.XPATH, orderId).text
        print ("order id is %s" % orderNumber)

        # 使用execute方法执行SQL语句
        order_id = orderNumber
        sql_order_id = "select * from user_order where id = '%s'" % order_id
        cursor.execute(sql_order_id)

        # 使用 fetchone() 方法获取一条数据库。
        results = cursor.fetchone()
        demand_type = results[23]
        print ("demand_type is %s" % demand_type)

        get_json = json.loads(demand_type)
        print get_json['isConfirm']
        confirmType = get_json['isConfirm']
        if confirmType == False:
            confirmType_xpath = '//*[@id="tpl-order"]/table/tbody/tr[2]/td[7]'
            text = self.browser.find_element(By.XPATH, confirmType_xpath).text
            self.assertEqual(text, u'非确认需求')
            print (u'经销商代理商未确认需求')

    def test_template_order(self):
        u"""我的订单重试状态检查"""
        # 模板化订单
        template_order_xpath = '//*[@id="category-top"]/div[1]/span'
        self.browser.find_element(By.XPATH, template_order_xpath).click()
        redo_time_xpath = '//*[@id="tpl-order"]/table/tbody/tr[2]/td[10]'
        redo_left = self.browser.find_element(By.XPATH, redo_time_xpath).text

        for i in range(int(redo_left)):
            want_redo_xpath = '//*[@id="tpl-order"]/table/tbody/tr[2]/td[11]/div[2]'
            want_redo = self.browser.find_element(By.XPATH, want_redo_xpath).text
            self.browser.find_element(By.XPATH, want_redo_xpath).click()
            comfirm_xpath = '//*[@id="confirm-pop-container"]/div[4]'
            self.browser.find_element(By.XPATH, comfirm_xpath).click()
            sleep(2)
            start_zhizuo_xpath = '//*[@id="videoMake-main"]/div[1]/div[2]/div[2]'
            self.browser.find_element(By.XPATH, start_zhizuo_xpath).click()
            comfirm1_xpath = '//*[@id="confirm-pop-container"]/div[4]'
            self.browser.find_element(By.XPATH, comfirm1_xpath).click()
            sleep(5)

            # 定制化订单
            dingzhi_xpath = '//*[@id="category-top"]/div[2]'
            self.browser.find_element(By.XPATH, dingzhi_xpath).click()
            sleep(10)
            template_order_xpath = '//*[@id="category-top"]/div[1]/span'
            self.browser.find_element(By.XPATH, template_order_xpath).click()
            redo_time_xpath = '//*[@id="tpl-order"]/table/tbody/tr[2]/td[10]'
            redon_left = self.browser.find_element(By.XPATH, redo_time_xpath).text
            print ("Redo number left is %d" % int(redon_left))
            if int(redon_left) == 1:
                function.insert_img(self.browser, "RedoNumLeft.jpg")
            if int(redon_left) == 0:
                want_redo_xpath = '//*[@id="tpl-order"]/table/tbody/tr[2]/td[11]/div[2]'
                want_redo = self.browser.find_element(By.XPATH, want_redo_xpath).text
                self.assertEqual(want_redo, u'导出到本地')
                function.insert_img(self.browser, "ExToLocal.jpg")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(MyOrder("test_custom_order"))
    suite.addTest(MyOrder("test_template_order"))

    results = unittest.TextTestRunner().run(suite)

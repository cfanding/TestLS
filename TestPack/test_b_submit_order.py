# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from selenium.webdriver.common.by import By
from utils import LSTest
import config
from time import sleep
import MySQLdb
import time


class SubmitOrder(LSTest):
    u"""模板商城提交订单集成数据库校验状态"""
    def test_submit_order(self):
        u"""模板商城提交订单集成数据库校验状态"""
        # url = config.Templates_URL
        # 模板商城
        # self.browser.get(url)
        # url = config.LOGIN_URL
        # self.login_into_page(url)

        sleep(5)
        # 个人场景
        personal_xpath = '//*[@id="category-top"]/div[1]/span'
        self.browser.find_element(By.XPATH, personal_xpath).click()
        third_xpath = '//*[@id="tpl-container"]/div/div[1]/div[1]'
        self.browser.find_element(By.XPATH, third_xpath).click()
        zhizuo_xpath = '//*[@id="data"]/div/div[2]/div'
        self.browser.find_element(By.XPATH, zhizuo_xpath).click()
        sleep(2)
        # 点击视频播放
        play_xpath = '//*[@id="videoMake-main"]/div[1]/div[1]/div[1]/div[1]/div'
        self.browser.find_element(By.XPATH, play_xpath).click()
        video = '//*[@id="video-object"]'
        video = self.browser.find_element(By.XPATH, video)

        # 返回播放文件地址
        url = self.browser.execute_script("return arguments[0].currentSrc;", video)
        print (url)

        # 播放10秒
        sleep(11)

        # 暂停视频
        print (u"暂停视频播放")
        self.browser.execute_script("arguments[0].pause()", video)

        # 截取当前页面播放记录
        self.browser.get_screenshot_as_file("D:\\TestLS\\report\\image\\play_10s.jpg")
        sleep(2)
        print (u"播放记录截图")
        # 关闭
        close_xpath = '//*[@id="video-player"]/div/div'
        self.browser.find_element(By.XPATH, close_xpath).click()

        # 输入内容
        shuru1_xpath = '//*[@id="videoMake-main"]/div[1]/div[1]/div[2]/div[1]/div[3]/div/textarea'
        self.browser.find_element(By.XPATH, shuru1_xpath).clear()
        self.browser.find_element(By.XPATH, shuru1_xpath).send_keys(u"自动化")
        # shuru2_xpath = '//*[@id="videoMake-main"]/div[1]/div[1]/div[2]/div[2]/div[3]/div/textarea'
        # self.browser.find_element(By.XPATH, shuru2_xpath).clear()
        # self.browser.find_element(By.XPATH, shuru2_xpath).send_keys("test2")

        # 滑动
        js = "window.scrollTo(0,744);"
        self.browser.execute_script(js)
        sleep(1)

        # 开始制作
        startmake_xpath = '//*[@id="videoMake-main"]/div[1]/div[2]/div[2]'
        self.browser.find_element(By.XPATH, startmake_xpath).click()

        # # 确定
        # confirm_xpath = '/html/body/div[1]/div[2]/div/div[4]'
        # self.browser.find_element(By.XPATH, confirm_xpath).click()
        # order确认
        order_confirm_xpath = '/html/body/div[1]/div[2]/div/div/div[5]/div[2]'
        self.browser.find_element(By.XPATH, order_confirm_xpath).click()

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
        order_status = results[19]
        print ("order status is %d"%order_status)

        order_status = 0

        while order_status != 3:
            conn = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME, port=3306, charset="utf8")
            time.sleep(20)
            sql_order_id = "select * from user_order where id = '%s'" % order_id
            cursor = conn.cursor()
            cursor.execute(sql_order_id)
            results = cursor.fetchone()
            order_status = results[19]
            cursor.close()
            conn.close()
            print (order_status)
            dingzhi_xpath = '//*[@id="category-top"]/div[2]/span'
            self.browser.find_element(By.XPATH, dingzhi_xpath).click()
            sleep(2)
            moban_xpath = '//*[@id="category-top"]/div[1]/span'
            self.browser.find_element(By.XPATH, moban_xpath).click()
            if order_status == 2:
                orderS_xpath = '//*[@id="tpl-order"]/table/tbody/tr[2]/td[9]'
                text = self.browser.find_element(By.XPATH, orderS_xpath).text
                self.assertEqual(text, '---')
                print (u"制作中")
            if order_status == 3:
                orderS_xpath = '//*[@id="tpl-order"]/table/tbody/tr[2]/td[9]/a'
                text = self.browser.find_element(By.XPATH, orderS_xpath).text
                self.assertEqual(text, u'点击预览')
                print (u"制作完成")
            if order_status == 4 or order_status == 5:
                orderS_xpath = '//*[@id="tpl-order"]/table/tbody/tr[2]/td[8]/div[2]'
                text = self.browser.find_element(By.XPATH, orderS_xpath).text
                self.assertEqual(text, u'点击可重试')
                print (u"制作失败")
                break
        print ("order status is  %d"%order_status)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(SubmitOrder("test_submit_order"))

    results = unittest.TextTestRunner().run(suite)

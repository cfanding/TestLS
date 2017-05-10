# -*- coding: utf-8 -*-
from selenium import webdriver
import os


# 截图函数
def insert_img(browser, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('// ', ' \ ')
    base = base_dir.split('\\TestPack')[0]
    file_path = base + "\\report\\image\\" + file_name
    browser.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get("http://www.baidu.com")
    insert_img(browser, 'baidu.jpg')
    browser.quit()


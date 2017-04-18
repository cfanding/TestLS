# -*- coding: utf-8 -*-

"Combine tests for gnosis.xml.objectify package (req 2.3+)"
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os

# ======定义发送邮件=====


def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')

    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.11.com', '25')
        smtp.login('cfanding@11.com', '**********')
        print("login success!")
    except smtplib.SMTPAuthenticationError:
        print("Authenticion error!")
    smtp.sendmail('cfanding@11.com', 'yading@11.com', msg.as_string())
    print ('email has send out !')
    smtp.quit()

# ======查找测试报告目录，找到最新生成的测试报告文件======


def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print (file_new)
    return file_new


if __name__ == '__main__':

    test_dir = 'D:\TestLS\TestPack'
    test_report = 'D:\\TestLS\\report'

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = test_report + '\\' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'乐声视频',
                            description=u'环境：windows 10 浏览器：chrome 56.0.2924.87')
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)  # 发送测试报告
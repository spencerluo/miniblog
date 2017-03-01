# coding=utf-8
import smtplib
import unittest
import multiprocessing
import time

import HTMLTestRunner
from email.mime.text import MIMEText

from keywords import keywords
from modules import login_module
from utils.log import Log


def createSuite():
    suite = unittest.TestSuite()

    case_path = r'D:\project\wangyiyun\autotest\test_cases'
    discover = unittest.defaultTestLoader.discover(case_path)

    for test_suite in discover:
        suite.addTest(test_suite)

    return suite


def sendMail(fileName):
    sender = '76421863@qq.com'
    receiver = 'wcnmbwsw@hotmail.com'
    server = 'smtp.qq.com'
    username = '76421863@qq.com'
    password = 'ljh68759058'

    report_file = open(fileName).read()
    msg = MIMEText(report_file, 'html', 'utf-8')
    msg['Subject'] = u'mini博客测试报告'

    smtp = smtplib.SMTP(server)
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.close()


def run(browserName, username, password):
    print u'开始运行测试'
    Log(browserName)
    keywords.browser = browserName
    login_module.username = username
    login_module.password = password
    all_cases = createSuite()
    date = time.strftime('%Y%m%d_%H%M%S')
    reportPath = r'D:\project\wangyiyun\autotest\reports\%s_%s.html' % (date, browserName)
    report = open(reportPath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(report, title=u'mimi博客', description=u'%s浏览器测试结果' % browserName)
    runner.run(all_cases)
    report.flush()
    # sendMail(reportPath)
    print u'测试结束'


def allRun():
    browsers = ['chrome', 'firefox']
    u = {'spencer', 'luojiahui'}
    p = ['asdD1234', 'asdD1234']
    processes = []
    for browser, username, password in zip(browsers, u, p):
        process = multiprocessing.Process(target=run, args=(browser, username, password))
        processes.append(process)
        process.start()
        for process in processes:
            process.join()


if __name__ == '__main__':
    # allRun()
    run('firefox','spencer','asdD1234')
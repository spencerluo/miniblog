# coding:utf-8

import unittest

import time

from keywords import keywords
from modules import login_module
from utils.log import Log


class Login(unittest.TestCase):
    def tearDown(self):
        self.driver.quit()
        Log.testEnd('Login')

    def setUp(self):
        Log.testStart('Login')
        self.driver = keywords.Webdriver()
        self.driver.openBrowser()

    def test_login(self):
        login_module.login(self.driver)
        time.sleep(2)
        self.assertIn(u'欢迎您，spencer~', self.driver.get_page_source())

    def testMyTest(self):
        print 'success'

if __name__ == '__main__':
    unittest.main()

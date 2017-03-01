# coding=utf-8
import unittest

import time

from keywords import keywords
from modules.login_module import login
from utils.log import Log


class WriteBlog(unittest.TestCase):
    def testWriteBlog(self):
        login(self.driver)
        time.sleep(2)
        self.driver.click('HomePage', 'Edit')
        self.driver.clear('EditPage', 'Title')
        self.driver.send_key('EditPage', 'Title', 'haha')
        self.driver.click('EditPage', 'Submit')
        time.sleep(2)
        self.assertIn(u'哈哈哈', self.driver.get_page_source())

    def tearDown(self):
        self.driver.quit()
        Log.testEnd('WriteBlog')

    def setUp(self):
        Log.testStart('WriteBlog')
        self.driver = keywords.Webdriver()
        self.driver.openBrowser()

if __name__ == '__main__':
    unittest.main()

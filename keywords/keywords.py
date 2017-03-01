from xml.dom import minidom
from utils.log import Log
from selenium import webdriver

browser = 'firefox'


class Webdriver:
    def __init__(self):
        self.driver = None
        self.dom = minidom.parse(r'D:\project\wangyiyun\autotest\document\element.xml')
        self.browser = browser

    def getElement(self, pageName, objectName):
        try:
            page = self.dom.getElementsByTagName(pageName)[0]
        except:
            Log.error('no such [%s]' % pageName)
            raise
        try:
            object = page.getElementsByTagName(objectName)[0]
        except:
            Log.error('no such [%s[' % objectName)
            raise
        type = object.getAttribute('type')
        value = object.getAttribute('value')
        element = None
        try:
            if type == 'id':
                element = self.driver.find_element_by_id(value)
            elif type == 'name':
                element = self.driver.find_element_by_name(value)
            elif type == 'class':
                element = self.driver.find_element_by_class_name(value)
            elif type == 'xpath':
                element = self.driver.find_element_by_xpath(value)
            elif type == 'linkText':
                element = self.driver.find_element_by_link_text(value)
            elif type == 'partialLinkText':
                element = self.driver.find_element_by_partial_link_text(value)
            else:
                Log.error('no such locate type [%s]' % type)
        except:
            Log.error("can't locate the element [%s] in [%s]" % (objectName, pageName))
            self.driver.get_screenshot_as_file(r'..\photos\%s_%s.png' % (objectName, pageName))
            raise
        return element

    def openBrowser(self):
        if self.browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif self.browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            Log.error('no such browser [%s]' % self.browser)
            raise Exception('no such browser [%s]' % self.browser)
        Log.info('open browser [%s]' % self.browser)

    def get(self, url):
        try:
            self.driver.get(url)
            Log.info('navigate to [%s]' % url)
        except:
            Log.error('can not navigate to [%s]' % url)
            raise

    def send_key(self, pageName, objectName, data):
        try:
            self.getElement(pageName, objectName).send_keys(data)
            Log.info('send [%s] to [%s] in [%s]' % (data, objectName, pageName))
        except:
            Log.error('can not send [%s] to [%s] in [%s]' % (data, objectName, pageName))
            raise

    def click(self, pageName, objectName):
        try:
            self.getElement(pageName, objectName).click()
            Log.info('click the [%s] in [%s]' % (objectName, pageName))
        except:
            Log.error('can not click the [%s] in [%s]' % (objectName, pageName))
            raise

    def clear(self, pageName, objectName):
        try:
            self.getElement(pageName, objectName).clear()
            Log.info('clear the [%s] in [%s]' % (objectName, pageName))
        except:
            Log.error('can not clear the [%s] in [%s]' % (objectName, pageName))
            raise

    def switch_to_frame(self, pageName, objectName):
        try:
            frame = self.getElement(pageName, objectName)
            self.driver.switch_to.frame(frame)
            Log.info('switch to [%s] in [%s]' % (objectName, pageName))
        except:
            Log.error('can not switch to [%s] in [%s]' % (objectName, pageName))
            raise

    def switch_to_default(self):
        self.driver.switch_to.default_content()
        Log.info('switch to default content')

    def get_page_source(self):
        return self.driver.page_source

    def quit(self):
        self.driver.quit()
        Log.info('close all windows')
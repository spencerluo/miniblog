import logging

import time


class Log:
    def __init__(self, browser):
        date = time.strftime('%Y%m%d_%H%M%S')
        logging.basicConfig(level=logging.INFO,
                            filename=r'd:\project\wangyiyun\autotest\logs\%s_%s.log' % (date, browser),
                            filemode='w')

    @staticmethod
    def info(data):
        logging.info(data)

    @staticmethod
    def error(data):
        logging.error(data)

    @staticmethod
    def testStart(data):
        logging.info('-' * 10 + data + ' test start' + '-' * 10)

    @staticmethod
    def testEnd(data):
        logging.info('-' * 10 + data + ' test end' + '-' * 10 + '\n')

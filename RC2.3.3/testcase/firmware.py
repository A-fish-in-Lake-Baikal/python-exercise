# coding=utf-8
import time
import unittest
import os.path
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from framework.browser_method import Browser_method

logger = Logger(logger="test_").getlog()


class MasterStation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """测试固件的setUp()的代码，主要是测试的前提准备工作"""
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """测试结束后的操作，这里基本上都是关闭浏览器"""
        logger.info("Now, Close and quit the browser.")
        cls.driver.quit()





if __name__ == '__main__':
    unittest.main()

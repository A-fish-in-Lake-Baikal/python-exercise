# coding=utf-8
# 新总站搜索结果功能
import time
import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from framework.browser_method import Browser_method

logger = Logger(logger="new master station page").getlog()


class Search(unittest.TestCase,Browser_method):

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        # logger.info("浏览器版本为：%s" %cls.get_version())

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        logger.info("Now, Close and quit the browser.")
        cls.driver.quit()

    def test_search1(self):
        u'''搜索关键字1'''
        self.driver.find_element_by_xpath("//*[@class='form-control' and @id='search-input']").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@class='form-control' and @id='search-input']").send_keys("1")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@class='btn png-icon search-icon']").click()
        logger.info("搜索")
        self.get_title()
        self.screen_sysrq("关键字1")
        time.sleep(2)
        self.back()
        logger.info("search success.")
        time.sleep(2)

    def test_search2(self):
        u'''搜索关键字test'''
        self.driver.find_element_by_xpath("//*[@class='form-control' and @id='search-input']").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@class='form-control' and @id='search-input']").send_keys("test")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@class='btn png-icon search-icon']").click()
        logger.info("搜索")
        self.get_title()
        self.screen_sysrq("关键字test")
        time.sleep(2)
        self.back()
        logger.info("search success.")
        time.sleep(2)

    def test_search3(self):
        u'''搜索关键字unit'''
        self.driver.find_element_by_xpath("//*[@class='form-control' and @id='search-input']").clear()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@class='form-control' and @id='search-input']").send_keys("unit")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@class='btn png-icon search-icon']").click()
        logger.info("搜索")
        self.get_title()
        self.screen_sysrq("关键字unit")
        time.sleep(2)
        self.back()
        logger.info("search success.")
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()
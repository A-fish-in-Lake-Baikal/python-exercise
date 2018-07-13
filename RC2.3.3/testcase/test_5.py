# coding=utf-8
import time
import unittest
import os.path
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from framework.browser_method import Browser_method

logger = Logger(logger="test_5").getlog()


class MasterStation(unittest.TestCase):
    '''进入站点首页点播资源'''
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        """
        logger.info("Now, Close and quit the browser.")
        cls.driver.quit()

    def test1(self):
        method = Browser_method(self.driver)
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[text()='所有站点']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@class='resouce_disc' and @title='综合']").click()
        time.sleep(1)
        num = self.driver.window_handles
        # 定位到新的标签页
        self.driver.switch_to.window(num[1])
        # 点击最新排行的模块
        self.driver.find_element_by_xpath("//*[@id='gotoNewRank']").click()
        method.screen_sysrq("二级页面——最新排行")
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@id='cate_new_upload_bar']").click()
        time.sleep(1)
        method.screen_sysrq("二级页面——最新上传")
        method.ScrollBar("1000")
        time.sleep(2)




if __name__ == '__main__':
    unittest.main()

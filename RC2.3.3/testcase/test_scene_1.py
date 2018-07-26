# coding=utf-8
import time
import unittest
import re
import os.path
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from framework.browser_method import Browser_method

logger = Logger(logger="test_scene_1").getlog()


class SceneOne(unittest.TestCase):
    '''验证资源平台所有页面的公司名称全部正确'''
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

    def test1(self):

        method = Browser_method(self.driver)
        txt = self.driver.find_element_by_xpath("//div[@class='col-xs-12 copyright']").text

        self.company_name(txt)

    def company_name(self,name):
        str = '北京传奇华育教育科技股份有限公司版权所有'
        if str in name:
            print("存在！")




if __name__ == '__main__':
    unittest.main()

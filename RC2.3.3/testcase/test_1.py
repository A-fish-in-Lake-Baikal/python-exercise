# coding=utf-8
import time
import unittest
import threading
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from framework.browser_method import Browser_method
from framework.module_one import Login

logger2 = Logger(logger="test_1").getlog()


class Search_Play(unittest.TestCase):
    '''用戶登陸后開始關鍵字搜索'''
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
        logger2.info("Now, Close and quit the browser.")
        cls.driver.quit()

        # 登录

    def test1(self):
        u'''登录后截取页面底部'''
        method = Browser_method(self.driver)
        self.driver.find_element_by_xpath("//*[@id='login_btn']/a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@id='login-name']").send_keys(r"user1001")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@id='login-pass']").send_keys("00000")
        self.driver.find_element_by_xpath("//*[@class='btn_c']").click()
        method.screen_sysrq("登录成功")
        record = self.driver.find_element_by_xpath("//*[@id='user_name']/a")
        method.mouse_click(4,record)
        time.sleep(3)
        method.ScrollBar(r"1000")
        method.screen_sysrq("页面最底部")

    def test2(self):
        '''根据人物名称搜索'''
        keys = ['王','李','林','1','12','3']
        for key in keys:
            method = Browser_method(self.driver)
            self.driver.find_element_by_xpath("//*[@id='search_input_master']").clear()
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='search_input_master']").send_keys(key)
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='search_btn_master']").click()
            method.screen_sysrq(key+"的搜索结果")
            time.sleep(2)
            logger2.info("search success.")
            method.back()

    def test3(self):
        '''资源播放和相关操作'''
        time.sleep(3)
        method = Browser_method(self.driver)
        self.driver.find_element_by_xpath("//*[text()='最新排行']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='hot_left']/div[1]/div/div/img").click()
        time.sleep(3)
        method.screen_sysrq("播放页")
        num = self.driver.window_handles  #获取当前窗口的句柄
        self.driver.switch_to.window(num[1])   #定位到最新的tab
        self.driver.find_element_by_xpath("//*[@class='glyphicon glyphicon-thumbs-up']").click()
        method.screen_sysrq("点赞后")
        method.alert_get()
        # self.driver.title
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
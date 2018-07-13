# coding=utf-8
import time
import unittest
import os.path
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from framework.browser_method import Browser_method
from selenium.common.exceptions import NoAlertPresentException

logger = Logger(logger="test_2").getlog()
username = 'mawc9'
realname = '马维畅9'

class Login(unittest.TestCase):
    '''注册成功之后使用注册的用户登录'''
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
        '''注册'''
        method = Browser_method(self.driver)
        self.driver.find_element_by_xpath("//*[@id='register_user' and text()='注册']").click() #注册按钮
        time.sleep(1)
        method.screen_sysrq("注册页面")
        self.driver.find_element_by_xpath("//*[@id='sign_in_agree' and text()='同意']").click() #同意条款
        self.driver.find_element_by_xpath("//*[@id='username']").send_keys(username)  #用户名
        self.driver.find_element_by_xpath("//*[@id='realname']").send_keys(realname)  #真实姓名
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys("00000")  #密码
        self.driver.find_element_by_xpath("//*[@id='repassword']").send_keys("00000")  #确认密码
        self.driver.find_element_by_xpath("//*[@id='department']").send_keys("测试部")  #部门
        self.driver.find_element_by_xpath("//*[@id='email']").send_keys("1564315@163.com")  # 邮箱
        self.driver.find_element_by_xpath("//*[@id='sign_in_btn']").click() #注册
        time.sleep(2)
        method.alert_get()  #关闭弹窗提示
        time.sleep(2)

    def test2(self):
        u'''登录'''
        method = Browser_method(self.driver)
        self.driver.find_element_by_xpath("//*[@id='login_btn']/a").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='login-name']").send_keys(username)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='login-pass']").send_keys("00000")
        self.driver.find_element_by_xpath("//*[@class='btn_c']").click()
        method.screen_sysrq("登录成功")
        time.sleep(2)





if __name__ == '__main__':
    unittest.main()

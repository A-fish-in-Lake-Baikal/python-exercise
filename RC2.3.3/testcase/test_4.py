# coding=utf-8
# coding=utf-8
import time
import unittest
import os.path
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from framework.browser_method import Browser_method
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import UnexpectedAlertPresentException

logger = Logger(logger="test_4").getlog()


class UserCneter(unittest.TestCase):
    '''验证是否能进入个人中心'''
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
        '''登录'''
        try:
            method = Browser_method(self.driver)
            self.driver.find_element_by_xpath("//*[@id='login_btn']/a").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@id='login-name']").send_keys("user8848")
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@id='login-pass']").send_keys("00000")
            self.driver.find_element_by_xpath("//*[@class='btn_c']").click()
            time.sleep(1)
            method.screen_sysrq("登录后！")
            if self.driver.find_element_by_xpath("//*[@class='glyphicon glyphicon-log-out']").is_displayed():
                logger.info("登录成功！")
            time.sleep(2)

        except ElementNotVisibleException as e:
            logger.error(e)
        except UnexpectedAlertPresentException as e:
            logger.error("登录失败！")
            logger.error(e)



    def test2(self):
        '''进入个人中心'''
        record = self.driver.find_element_by_xpath("//*[@id='user_name']/a").click()
        time.sleep(1)
        if self.driver.find_element_by_xpath("//*[@class='uc_logo']").is_displayed():
            logger.info("成功进入个人中心")
        else:
            logger.error("进入失败！")





if __name__ == '__main__':
    unittest.main()
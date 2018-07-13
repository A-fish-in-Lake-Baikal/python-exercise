import time
from framework.logger import Logger
from framework.browser_method import Browser_method

class Login(object):
    def __init__(self,driver):
        self.driver = driver

    def log_in(self,name,pwd):
        self.driver.find_element_by_xpath("//*[@class='png-icon login-btn']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='login-username']").send_keys(name)
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='login-password']").send_keys(pwd)
        self.driver.find_element_by_xpath("//*[@id='login-btn']").click()

    def log_out(self):
        method = Browser_method(self.driver)
        record = self.driver.find_element_by_xpath("/html/body/header/div/ul[2]/li[5]/span")
        method.mouse_hover(record)
        self.driver.find_element_by_xpath("//ul[@class='dropdown-menu user-dropdown-menu']/li[7]/a").click()
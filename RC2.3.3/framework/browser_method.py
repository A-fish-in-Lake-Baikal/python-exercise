# 浏览器常用操作方法
import time
import os.path
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from framework.logger import Logger
from selenium.common.exceptions import NoAlertPresentException

logger = Logger(logger="browser_method").getlog()

class Browser_method(object):

    def __init__(self,driver):
        self.driver=driver

# 浏览器操作
    # 返回上一页
    def back(self):
        self.driver.back()
        logger.info("后退")

    # 前进
    def forward(self):
        self.driver.forward()
        logger.info("前进")

    # 刷新
    def refresh(self):
        self.driver.refresh()
        logger.info("刷新页面")

    # 滚动条
    def ScrollBar(self,num):
        js_ = "self.document.documentElement.scrollTop="+num   #num值为零滚动到页面顶部，大于浏览器高度则为最底部
        self.driver.execute_script(js_)
        logger.info("滚动%s像素" %num)

    # 进入iframe
    def go_iframe(self,frame):
        self.driver.switch_to.frame(frame)
        logger.info("进入frame %s" %frame)

    # 退出iframe
    def exit_iframe(self):
        self.driver.switch_to.default_content()
        logger.info("退出iframe")

    # 打开一个新的tab
    def new_tab(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'T') #  触发ctrl + t
        logger.info("新建tab")

    # 获取当前页面的title
    def get_title(self):
        title= self.driver.title
        logger.info(title)
        '''t = self.driver.title'''
        return title

    # 获取浏览器版本号
    def get_version(self):
        logger.info(self.driver.capabilities['version'])

    # 截图
    def screen_sysrq(self,name):
        file_path = os.path.dirname(os.getcwd()) + '/Screenshots/'
        try:
            self.driver.get_screenshot_as_file(file_path+name+'.png')
            logger.info(u"开始截图并保存")

        except Exception as e:
            # logger.error(u"出现异常", format(e))
            pass

    # alert弹出窗处理并返回提示信息
    def alert_get(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            logger.info(alert_text)
            return alert_text
        except NoAlertPresentException as e:
            logger.error(format(e))




# 鼠标方法

    def mouse_click(self,status,name):
        if status == 1:
            #右击context_click()
            ActionChains(self.driver).context_click(name).perform()
            logger.info("鼠标右击")

        elif status == 2:
            #     双击double_click()
            ActionChains(self.driver).double_click(name).perform()
            logger.info("鼠标双击")

        elif status == 3:
            #     拖动drag_and_drop()
            ActionChains(self.driver).drag_and_drop(name).perform()
            logger.info("鼠标拖动")

        elif status == 4:
            #     鼠标悬停move_to_element()
            ActionChains(self.driver).move_to_element(name).perform()
            logger.info("鼠标悬停")
        else:
            logger.info("输入错误！")

# 操作cookie
    #获取cookie
    def get_cookie(self):
        cookie = self.driver.get_cookies()
        logger.info(cookie)
        return cookie
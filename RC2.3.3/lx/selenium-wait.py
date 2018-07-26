from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get('https://www.toutiao.com/')
# 判断元素是否是可点击的
try:
    element = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.CLASS_NAME,"login-button"))
    )
    print("success")
except TimeoutException:
    print("undefind")




finally:
    driver.quit()
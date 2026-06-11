
from selenium import webdriver

driver = webdriver.Edge()

driver.get("http://www.baidu.com")

import time
time.sleep(3)

driver.quit()

import time

import pytest
from selenium import webdriver
import yaml

@pytest.fixture(scope="module")
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit()

# 定义selenium夹具，类似于重写
@pytest.fixture()
def selenium(request, driver):
    request.node._driver = driver # 把浏览器给到当前用例
    yield driver

# 装饰器
def ddt(yaml_path, **kwargs):
    f = open(yaml_path, "r", encoding="utf-8")
    data_list = yaml.safe_load(f)
    return pytest.mark.parametrize("data", data_list, **kwargs)


# web自动化
@ddt("syn/ddt_login.yaml")
def test_web(selenium, data):
    selenium.get("http://116.62.63.211/shop/?s=user/loginInfo.html")

    el_username = selenium.find_element('xpath', '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input')
    el_password = selenium.find_element('xpath', '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input')
    el_submit = selenium.find_element('xpath', '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button')

    el_username.send_keys(data['username'])
    el_password.send_keys(data['password'])
    el_submit.click()

    time.sleep(1)

    sys_info = selenium.find_element('xpath','/html/body/div[10]/div/p').text

    assert sys_info == data['msg']
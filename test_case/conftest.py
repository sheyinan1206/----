import base64
import datetime
import time

import allure
import pytest


@pytest.fixture(scope='package')
def sheyn():

    print('用例开始时间：',datetime.datetime.now())

    #前置操作
    # time.sleep(1)
    yield '我是syn'  #生成器

    #后置操作
    print('用例结束时间：',datetime.datetime.now())

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    自动将Selenium截图附加到Allure报告
    """
    outcome = yield
    rep = outcome.get_result()
    

    # 获取driver对象
    driver = item.funcargs.get('driver') or item.funcargs.get('selenium')
    
    if driver:
        try:
            # 捕获截图并附加到Allure报告
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"截图_{datetime.datetime.now().strftime('%H%M%S')}",
                attachment_type=allure.attachment_type.PNG
            )
            print("\n✓ 截图已附加到Allure报告")
        except Exception as e:
            print(f"\n✗ 截图失败: {str(e)}")
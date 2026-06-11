import base64
import datetime
import time

import pytest


@pytest.fixture(scope='package')
def sheyn():

    print('用例开始时间：',datetime.datetime.now())

    #前置操作
    # time.sleep(1)
    yield '我是syn'  #生成器

    #后置操作
    print('用例结束时间：',datetime.datetime.now())


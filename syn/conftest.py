import datetime

import pytest


@pytest.fixture(scope='package')
def sheyn():

    print('用例开始时间：',datetime.datetime.now())

    #前置操作
    yield   #生成器

    #后置操作
    print('用例结束时间：',datetime.datetime.now())

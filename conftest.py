import datetime
import time

import pytest


@pytest.fixture(scope='package')
def sheyn():

    print('start time',datetime.datetime.now())

    #前置操作
    time.sleep(1)
    yield   #生成器

    #后置操作
    print('end time',datetime.datetime.now())

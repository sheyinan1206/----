
import datetime
import time

import pytest

def test_syn(sheyn,data):
    print('我是测试用例，正在执行')
    data['msg']= '我是第一个用例'

@pytest.fixture(scope='session')
def data():
    return {} #可变对象

@pytest.fixture(scope='function')
def sheyn():

    print('start time',datetime.datetime.now())

    #前置操作
    time.sleep(1)
    yield '我是syn'  #生成器

    #后置操作
    print('end time',datetime.datetime.now())


# #用例中使用
# @pytest.mark.usefixtures('sheyn')
# def test_sheyn1():
#     print('我是测试用例1，正在执行')
    

# #参数使用
# def test_sheyn2(sheyn):
#     print('我是测试用例2，正在执行')
#     pass

class TestUser:

    @pytest.fixture(scope='function')
    def sheyn(self):

        print('xxxx',datetime.datetime.now())

        

        #前置操作
        time.sleep(1)
        yield 'i am syn'  #生成器

        #后置操作
        print('xxxx',datetime.datetime.now())

    @pytest.mark.order(1)     
    def test_web(self,sheyn,data):
        print(sheyn)

        print('上一个用例传递的内容是：',data['msg'])
        data['msg']= '我是第二个用例'
        print('当前用例传递的内容是：',data['msg'])

    @pytest.mark.order(3)     
    def test_api(self,sheyn,data):
        print(sheyn)
        print('上一个用例传递的内容是：',data['msg'])
        data['msg']= '我是第三个用例'
        print('当前用例传递的内容是：',data['msg'])

    @pytest.mark.order(2)     
    def test_ut(self,sheyn,data):
        print(sheyn)   
        print('上一个用例传递的内容是：',data['msg'])
        data['msg']= '我是第四个用例'
        print('当前用例传递的内容是：',data['msg'])

class TestGoods:
     
    def test_web(self,sheyn,data):
        print(sheyn)
        print('上一个用例传递的内容是：',data['msg'])
        data['msg']= '我是第五个用例'
        print('当前用例传递的内容是：',data['msg'])
     
    def test_api(self,sheyn,data):
        print(sheyn)
        print('上一个用例传递的内容是：',data['msg'])
        data['msg']= '我是第六个用例'
        print('当前用例传递的内容是：',data['msg'])


    def test_ut(self,sheyn,data):
        print(sheyn)
        print('上一个用例传递的内容是：',data['msg'])
        data['msg']= '我是第七个用例'
        print('当前用例传递的内容是：',data['msg'])


import datetime

import pytest



#用例中使用
@pytest.mark.usefixtures('sheyn')
def test_sheyn1():
    print('我是测试用例1，正在执行')
    

#参数使用
def test_sheyn2(sheyn):
    print('我是测试用例2，正在执行')
    pass

class TestUser:
     
    def test_web(self,sheyn):
        pass
     
    def test_api(self,sheyn):
        pass

    def test_ut(self,sheyn):
        pass

class TestGpods:
     
    def test_web(self,sheyn):
        pass
     
    def test_api(self,sheyn):
        pass

    def test_ut(self,sheyn):
        pass
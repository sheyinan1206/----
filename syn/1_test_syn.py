import pytest

def test_web():
    assert 1 == 1
    return None

def test_api():
    assert 1 == 2

def test__pass():
    assert 1 == 1

def test__fail():
    a = ['asdfasdfasdfasdfasdfasdfa','12314',213];
    b = ['asdfasdfasdcdsdfasdfasdfa','qweqwe',2];
    assert a == b

@pytest.fixture()
def f():
    assert 1==2

def test_error(f):
    assert 1 == 3

@pytest.mark.skip
def test_skip():
    assert 1==2

@pytest.mark.xfail
def test_xpass():
    pass

@pytest.mark.xfail
def test_xfail():
    assert 1==2

class TestSyn:
    # def __init__(self):
    #     pass
    n = 1
    @pytest.mark.api
    def test_v1(self):
        m = int(input('我是：'))
        assert 1 == m
        print('我是v1')
        
    @pytest.mark.web
    def test_v2(self):
        assert 1 == self.n
        print('我是v2')
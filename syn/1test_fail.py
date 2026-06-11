import random

import pytest
import yaml


# 封装DDT装饰器
def ddt(yaml_path, **kwargs):
    f = open(yaml_path, "r", encoding="utf-8")
    data_list = yaml.safe_load(f)
    return pytest.mark.parametrize("data", data_list, **kwargs)





@ddt("data.yaml")
def test_fail1(data):
    assert 1==data


@ddt("data.yaml")
def test_fail2(data):
    assert 2==data

# f = open("data.yaml", "r", encoding="utf-8")
# data = yaml.safe_load(f)

# @pytest.mark.parametrize(
#     data
# )
# def test_fail(m):
#     assert 1==m


# web自动化
def test_web(selenium):
    selenium.get("http://www.baidu.com")
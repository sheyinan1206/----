import random

import pytest

def test_fail():
    assert 1==random.randint(1,3)
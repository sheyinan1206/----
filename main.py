import pytest

import os

import shutil

shutil.rmtree('report', ignore_errors=True)
shutil.rmtree('temps', ignore_errors=True)

pytest.main()
os.system("allure generate -o report -c temps")
import calculate
# to run pytest -v -rxs test_calculate.py
# we import the pytest to used as decorator
import pytest


@pytest.mark.skip(reason="I do not wat to run this test function for now")
def test_divide():
	total = calculate.divide(64, 8)
	assert total == 8

def test_multiply():
	output = calculate.multiply(8, 7)
	assert output == 56

'''
OUTPUT
platform linux -- Python 3.5.2, pytest-3.4.1, py-1.5.2, pluggy-0.6.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/dilmac/DevOP/tutorials/Python/Pytest, inifile:
collected 2 items                                                                                                                                                                                 

test_calculate.py::test_divide SKIPPED                                                                                                                                                      [ 50%]
test_calculate.py::test_multiply PASSED                                                                                                                                                     [100%]
===================================================================================== short test summary info =====================================================================================
SKIP [1] test_calculate.py:7: unconditional skip
'''
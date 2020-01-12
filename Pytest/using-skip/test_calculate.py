'''
Skip test
Selectivly runtests using their name
Custom markers

How this work:
1. import mathlib or calculate
2. import pytest # to use as decorator
3. Add decorator to the method you want to skip from running:
@pytest.mark.skip(reason="I do not wat to run this test function for now")

This command will run the test and skip the method you don't want to test
pytest -v test_calculate.py 

pytest -v using-skip/test_calculate.py 
==================================================================== test session starts =====================================================================
platform linux2 -- Python 2.7.17, pytest-3.3.2, py-1.5.2, pluggy-0.6.0 -- /usr/bin/python2
cachedir: .cache
rootdir: /home/raffi/Devel/Python/Pytest, inifile:
collected 2 items                                                                                                                                            

using-skip/test_calculate.py::test_divide SKIPPED                                                                                                      [ 50%]
using-skip/test_calculate.py::test_multiply PASSED                                                                                                     [100%]

============================================================ 1 passed, 1 skipped in 0.01 seconds =============================================================


This command will run the test and skip the method but show you the reason
pytest -v -rxs test_calculate.py

pytest -v -rxs using-skip/test_calculate.py 
==================================================================== test session starts =====================================================================
platform linux2 -- Python 2.7.17, pytest-3.3.2, py-1.5.2, pluggy-0.6.0 -- /usr/bin/python2
cachedir: .cache
rootdir: /home/raffi/Devel/Python/Pytest, inifile:
collected 2 items                                                                                                                                            

using-skip/test_calculate.py::test_divide SKIPPED                                                                                                      [ 50%]
using-skip/test_calculate.py::test_multiply PASSED                                                                                                     [100%]
================================================================== short test summary info ===================================================================
SKIP [1] using-skip/test_calculate.py:26: I do not wat to run this test function for now

============================================================ 1 passed, 1 skipped in 0.01 seconds =============================================================

'''

import calculate
# to run pytest -v -rxs test_calculate.py
# we import the pytest to used as decorator
import pytest
# use sys to test different reson like python version
import sys


@pytest.mark.skip(reason="I do not wat to run this test function for now")
def test_divide():
    total = calculate.divide(64, 8)
    assert total == 8


def test_multiply():
    output = calculate.multiply(8, 7)
    assert output == 56


# Import sys and added the if at the end of skip
# Example: skipif(sys.version_info Not equal to 3.6 I have 3.7 version
# this test skip because my version is bigger then 3.6 to make it Passthe test
# change skipif(sys.version_info == (3.7))
@pytest.mark.skipif(sys.version_info != (3.6),
                    reason="I do not wat to test this method because of the python version != 3.6")
def test_substruct_method():
    total = calculate.substruct_method(19, 8)
    assert total == 11


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

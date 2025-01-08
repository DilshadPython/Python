import using_skipif
# to run pytest -v -rxs test_calculate.py
# if I want to run only one function like divid as an example we run
# pytest -k divid or pytest -k multiply
# we import the pytest to used as decorator
import pytest
# we import the sys to version
import sys

# we change skip to skipif and tell if the python version is < (3,5) than not working to test
# change the python to sys.version_info < (3,5) it will passed


@pytest.mark.skipif(sys.version_info > (3, 5), reason="This test will skip because of python version")
def test_divide():
    total = using_skipif.divide(64, 8)
    assert total == 8


def test_multiply():
    output = using_skipif.multiply(8, 7)
    assert output == 56


''' Notce 
if I run this command pytest -v -rxs test_calculate_1.py all passed and skip doesn't work
but if I run pytest -v -rxs  here is the layout
======================================= test session starts =================================
======================================= test session starts =================================
cachedir: .pytest_cache
rootdir: /home/dilmac/DevOP/tutorials/Python/Pytest, inifile:
collected 2 items                                                                                                                                                                                 

test_using_skipif.py::test_divide SKIPPED                                                                                                                                                   
test_using_skipif.py::test_multiply PASSED                                                                                                                                                 
======================================== short test summary info ============================
SKIP [1] test_using_skipif.py:10: This test will skip because of python version


pytest -k multiply
dilmac@dilmac-ViB ~/DevOP/tutorials/Python/Pytest $ pytest -k multiply
======================================== test session starts ================================
platform linux -- Python 3.5.2, pytest-3.4.1, py-1.5.2, pluggy-0.6.0
rootdir: /home/dilmac/DevOP/tutorials/Python/Pytest, inifile:
collected 8 items                                                                                                                                                                                 

test_calculations.py .                                                                                                                                                                     
test_using_skipif.py .                                                                                                                                                                 
using-skip/test_calculate.py .                                                                                                                                                            

======================================= 5 tests deselected ==================================
======================================= 3 passed, 5 deselected in 0.05 seconds =


'''

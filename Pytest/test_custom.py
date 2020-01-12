import custom
import pytest


@pytest.mark.custom
def test_custom_multiply():
    result = custom.custom_multiply(45, 4)
    assert result == 180


@pytest.mark.custom
def test_custom_plus():
    result = custom.custom_plus(4, 34)
    assert result == 38


@pytest.mark.example
def test_example_divide():
    result = custom.example_divide(24, 4)
    assert result == 6


@pytest.mark.example
def test_example_substruct():
    result = custom.example_substruct(9, 7)
    assert result == 2


'''
To test this method we test only those methods has word custom in:

pytest -m custom test_custom.py
==================================================================== test session starts =====================================================================
platform linux2 -- Python 2.7.17, pytest-3.3.2, py-1.5.2, pluggy-0.6.0
rootdir: /home/raffi/Devel/Python/Pytest, inifile:
collected 4 items                                                                                                                                            

test_custom.py ..                                                                                                                                      [100%]

===================================================================== 2 tests deselected =====================================================================
=========================================================== 2 passed, 2 deselected in 0.01 seconds ===========================================================
raffi@raffi-VB:~/Devel/Python/Pytest$ pytest -m custom test_custom.py -v
==================================================================== test session starts =====================================================================
platform linux2 -- Python 2.7.17, pytest-3.3.2, py-1.5.2, pluggy-0.6.0 -- /usr/bin/python2
cachedir: .cache
rootdir: /home/raffi/Devel/Python/Pytest, inifile:
collected 4 items                                                                                                                                            

test_custom.py::test_custom_multiply PASSED                                                                                                            [ 50%]
test_custom.py::test_custom_plus PASSED                                                                                                                [100%]

===================================================================== 2 tests deselected =====================================================================
=========================================================== 2 passed, 2 deselected in 0.01 seconds ===========================================================
raffi@raffi-VB:~/Devel/Python/Pytest$ 

# Here we test only those methods has words example in it:
pytest -m example test_custom.py -v
==================================================================== test session starts =====================================================================
platform linux2 -- Python 2.7.17, pytest-3.3.2, py-1.5.2, pluggy-0.6.0 -- /usr/bin/python2
cachedir: .cache
rootdir: /home/raffi/Devel/Python/Pytest, inifile:
collected 4 items                                                                                                                                            

test_custom.py::test_example_divide PASSED                                                                                                             [ 50%]
test_custom.py::test_example_substruct PASSED                                                                                                          [100%]

===================================================================== 2 tests deselected =====================================================================
=========================================================== 2 passed, 2 deselected in 0.01 seconds ===========================================================
raffi@raffi-VB:~/Devel/Python/Pytest$ 

'''

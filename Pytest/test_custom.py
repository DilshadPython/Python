import custom
import pytest


def test_custom_multiply():
    result = custom.custom_multiply(45, 4)
    assert result == 180

'''
Important
This pytest using old version of python2.7 when run the test
display an warning after the test to avoid the warning just 
comment out this line

pytest -v -rxs test_custom.py 
pytest -v test_custom.py 

/usr/local/lib/python2.7/dist-packages/_pytest/mark/structures.py:335
  /usr/local/lib/python2.7/dist-packages/_pytest/mark/structures.py:335: PytestUnknownMarkWarning: Unknown pytest.mark.using_skipif - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    PytestUnknownMarkWarning,

-- Docs: https://docs.pytest.org/en/latest/warnings.html

'''
# @pytest.mark.custom
def test_custom_plus():
    result = custom.custom_plus(4, 34)
    assert result == 38


# @pytest.mark.example
def test_example_divide():
    result = custom.example_divide(24, 4)
    assert result == 6


# @pytest.mark.example
def test_example_substruct():
    result = custom.example_substruct(9, 7)
    assert result == 2


# @pytest.mark.custom
def test_add_num():
    output = custom.add_num(3, 5)
    output_1 = custom.add_num(7)
    output_2 = custom.add_num(21)

    assert output == 8
    assert output_1 == 10
    assert output_2 == 24


# @pytest.mark.custom
def test_multi_num():
    output = custom.multi_num(3, 5)
    output_1 = custom.multi_num(6)
    output_2 = custom.multi_num(37)

    assert output == 15
    assert output_1 == 12
    assert output_2 == 74


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

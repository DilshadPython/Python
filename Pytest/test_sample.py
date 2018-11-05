import sample


def test_myfunc():
    y = 7 + 2
    assert y == 9


def test_hello():
    assert True

''''
I test only function contain myfunc
dilmac@dilmac-ViB ~/DevOP/tutorials/Python/Pytest $ pytest -k myfunc -v
================================= test session starts ====================================
platform linux -- Python 3.5.2, pytest-3.4.1, py-1.5.2, pluggy-0.6.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/dilmac/DevOP/tutorials/Python/Pytest, inifile:
collected 8 items                                                                                                                                                                                 

test_sample.py::test_myfunc PASSED                                                                                                                                                        

================================== 7 tests deselected ====================================
============================== 1 passed, 7 deselected in 0.03 seconds ====================
'''

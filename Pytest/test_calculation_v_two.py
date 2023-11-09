import calculations

'''
pytest -v test_calculation_v_tewo.py
The command above run the verbos which is mean the name or the file
including the result like below:

Pytest$ pytest -v test_calculation_v_two.py 
=============== test session starts ===============
platform linux2 -- Python 2.7.17, pytest-3.3.2, py-1.5.2, pluggy-0.6.0 -- /usr/bin/python2
cachedir: .cache
rootdir: /home/raffi/Devel/Python/Pytest, inifile:
collected 1 item                                                                                                                                             

test_calculation_v_two.py::test_adding PASSED                                                                                                          [100%]

=============== 1 passed in 0.01 seconds ===============
'''


def test_adding():
    result = calculations.adding(7, 19)
    return result


# if you run this command
# pytest -k substracting it will test only this method named substracting
def test_substracting():
    result = calculations.substracting(9, 44)
    return result


'''
 pytest -k substracting test_calculation_v_two.py 
==================================================================== test session starts =====================================================================
platform linux2 -- Python 2.7.17, pytest-3.3.2, py-1.5.2, pluggy-0.6.0
rootdir: /home/raffi/Devel/Python/Pytest, inifile:
collected 2 items                                                                                                                                            

test_calculation_v_two.py .                                                                                                                            [100%]

===================================================================== 1 tests deselected =====================================================================
=========================================================== 1 passed, 1 deselected in 0.01 seconds ===========================================================
'''


'''
The function below is extra false ro make it run and see how the test faild 
this is what is happening:
 pytest -v test_calculation_v_two.py 
=============== test session starts ===============
platform linux2 -- Python 2.7.17, pytest-3.3.2, py-1.5.2, pluggy-0.6.0 -- /usr/bin/python2
cachedir: .cache
rootdir: /home/raffi/Devel/Python/Pytest, inifile:
collected 2 items                                                                                                                                            

test_calculation_v_two.py::test_adding PASSED                                                                                                          [ 50%]
test_calculation_v_two.py::test_substracting FAILED                                                                                                    [100%]

=============== FAILURES ====================
_______________ test_substracting _______________

    def test_substracting():
>   	result = calculations.substracting('w', 44)

test_calculation_v_two.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

firstnumber = 'w', secondnumber = 44

    def substracting(firstnumber, secondnumber):
>       result = firstnumber - secondnumber
E       TypeError: unsupported operand type(s) for -: 'str' and 'int'

calculations.py:10: TypeError
=============== 1 failed, 1 passed in 0.03 seconds ===============
'''

# You can't substruct strin to integer!!
# def test_substracting():
# 	result = calculations.substracting('w', 44)
# 	return result


'''
We created extra function has word func in it and running this command
pytest -k func test_calculation_v_two.py -v
'''


def test_func_fake():
    assert True


'''
OUTPUT

pytest -k func test_calculation_v_two.py -v
=============== test session starts ===============
platform linux2 -- Python 2.7.17, pytest-3.3.2, py-1.5.2, pluggy-0.6.0 -- /usr/bin/python2
cachedir: .cache
rootdir: /home/raffi/Devel/Python/Pytest, inifile:
collected 3 items                                                                                                                                            

test_calculation_v_two.py::test_func_fake PASSED                                                                                                       [100%]

=============== 2 tests deselected ===============
=============== 1 passed, 2 deselected in 0.01 seconds ===============
'''

# to run all methods test run this command
# pytest -v test_calculation_v_two

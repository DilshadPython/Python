### Use skipif 
/Pytest $ pytest -v -rxs test_using_skipif.py 
============================================= test session starts =======================================================================================
platform linux -- Python 3.5.2, pytest-3.4.1, py-1.5.2, pluggy-0.6.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/dilmac/DevOP/tutorials/Python/Pytest, inifile:
collected 2 items                                                                                                                                                                                 

test_using_skipif.py::test_divide SKIPPED                                                                                                                                                 
test_using_skipif.py::test_multiply PASSED                                                                                                                                                  
========================================== short test summary info =========================================================================
SKIP [1] test_using_skipif.py:10: This test will skip because of python version

=============================================================================== 1 passed, 1 skipped in 0.02 seconds ===============================================================================
                                                                                                                                               
### Changed the python version < (3,5)
/Pytest $ pytest -v -rxs test_using_skipif.py 
======================================================== test session starts =======================================================================================
platform linux -- Python 3.5.2, pytest-3.4.1, py-1.5.2, pluggy-0.6.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/dilmac/DevOP/tutorials/Python/Pytest, inifile:
collected 2 items                                                                                                                                                                                 

test_using_skipif.py::test_divide SKIPPED                                                                                                                                                   
test_using_skipif.py::test_multiply PASSED                                                                                                                                                  
================================ short test summary info =====================================================================================
SKIP [1] test_using_skipif.py:10: This test will skip because of python version

=============================================================================== 1 passed, 1 skipped in 0.01 seconds 

### Use -k to run only the test required with the name or select one word in the func
/Pytest $ pytest -k test_using_skipif.py 
======================================================================================= test session starts =======================================================================================
platform linux -- Python 3.5.2, pytest-3.4.1, py-1.5.2, pluggy-0.6.0
rootdir: /home/dilmac/DevOP/tutorials/Python/Pytest, inifile:
collected 8 items                                                                                                                                                                                 

test_using_skipif.py s.                                                                                                                                                                   

=============================================== 6 tests deselected ========================================================================================
============================================== 1 passed, 1 skipped, 6 deselected in 0.06 seconds ========================================================================

### Run only function in the file contain multiply
/Pytest $ pytest -k multiply
======================================================================================= test session starts =======================================================================================
platform linux -- Python 3.5.2, pytest-3.4.1, py-1.5.2, pluggy-0.6.0
rootdir: /home/dilmac/DevOP/tutorials/Python/Pytest, inifile:
collected 8 items                                                                                                                                                                                 

test_calculations.py .                                                                                                                                                                      
test_using_skipif.py .                                                                                                                                                                     
using-skip/test_calculate.py .                                                                                                                                                              
========================================== 5 tests deselected ========================================================================================
============================================================================= 3 passed, 5 deselected in 0.05 seconds ==============================================================================

### Use -k to run the function contain multiply and use -v to display the file names
/Pytest $ pytest -k multiply -v
======================================================================================= test session starts =======================================================================================
platform linux -- Python 3.5.2, pytest-3.4.1, py-1.5.2, pluggy-0.6.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/dilmac/DevOP/tutorials/Python/Pytest, inifile:
collected 8 items                                                                                                                                                                                 

test_calculations.py::test_multiply PASSED                                                                                                                                                 
test_using_skipif.py::test_multiply PASSED                                                                                                                                                  
using-skip/test_calculate.py::test_multiply PASSED                                                                                                                                          

============================================ 5 tests deselected============================================================
============================================ 3 passed, 5 deselected in 0.06 seconds 
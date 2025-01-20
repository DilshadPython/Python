### To check unittest 

#### import unittest
#### help(unittest)

# Using pytest 
sudo apt install python3-pytest

pytest test_number.py

# Runing
 pytest test_example.py 
============================================================================================== test session starts ==============================================================================================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/dilmac/Dev/Python/unittest
collected 1 item                                                                                                                                                                                                

test_example.py .                                                                                                                                                                                         [100%]

=============================================================================================== 1 passed in 0.01s ===============================================================================================

# We have create folder named test and create another test_message.py with some small change
# to testing with pytest we can run pytest test because we create __init__.py this folder now
# is package we can tested with the test folder name
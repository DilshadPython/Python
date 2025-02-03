# we use _ for lname which is means we try to unpack here if don't put the lname
# it shows me an error because it has to be two value but if I enter both display
# the fname because this is what requested in print

Testing:
py unpack.py
What is your name? Dilshad Abdulla
Welcome back, Dilshad!

Testing:
py unpack.py
What is your name? Dilshad
Traceback (most recent call last):
  File "/home/Python/Unpack/unpack.py", line 4, in <module>
    fname, _ = input("What is your name? ").split(' ')
    ^^^^^^^^
ValueError: not enough values to unpack (expected 2, got 1)

# Testing coins_error.py
py coins.py
Unpack/coins.py", line 9, in <module>
    print(total(coins), 'Inch')
          ^^^^^^^^^^^^
TypeError: total() missing 2 required positional arguments: 'width' and 'height'

Info:
The *coins it works only for list not set, no tuple and no dict
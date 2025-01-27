example.py
Here we just created class with full empty data and without any methods like
# __init__ or __str__ and __repr__. etc ...
The goal here is to understand how to create a class and to make it easy to
work type ... to show class is created and the program is running

#################################################################
example_1.py

ere we have define the __init__ method which is called initialization of the class
dunder __init__(self) which is instance methods
we define the data we want like first name and last name and age

This is the initialization of the class this method will automatic called by class object

Run:
py example_1.py
Enter your first name: Dilshad
Enter your last name: Abdulla
Enter your age: 51
Full name is: Dilshad Abdulla 51 years old

py example_2.py
Enter your first name: Dill
Enter your last name: Abdulla
Enter your age: 52
Full name is: Dill Abdulla 52 years old

py example_2.py
Enter your first name:
Enter your last name:
Enter your age: 23
Traceback (most recent call last):
  File "/home/dilmac/Dev/Python/OOProgrammingH/Classes/example_2.py", line 27, in <module>
    main()
  File "/home/dilmac/Dev/Python/OOProgrammingH/Classes/example_2.py", line 14, in main
    user = get_user()
           ^^^^^^^^^^
  File "/home/dilmac/Dev/Python/OOProgrammingH/Classes/example_2.py", line 23, in get_user
    return User(first_name, last_name, age)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dilmac/Dev/Python/OOProgrammingH/Classes/example_2.py", line 6, in __init__
    raise ValueError("First name and last name cannot be empty")
ValueError: First name and last name cannot be empty

You can create or changed your own error like DillError instead of ValueError

#################################################################
We are create __str__() method to be able to print the data in the class object like
user = User(first_name, last_name)
print(user)

testing:
py example_3.py
Enter your first name: Dilshad
Enter your last name: Adam
Traceback (most recent call last):
  File "/home/dilmac/Dev/Python/OOProgrammingH/Classes/example_3.py", line 31, in <module>
    main()
  File "/home/dilmac/Dev/Python/OOProgrammingH/Classes/example_3.py", line 18, in main
    user = get_user()
           ^^^^^^^^^^
  File "/home/dilmac/Dev/Python/OOProgrammingH/Classes/example_3.py", line 27, in get_user
    return User(first_name, last_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dilmac/Dev/Python/OOProgrammingH/Classes/example_3.py", line 8, in __init__
    raise ValueError("The last name is not in the list")
ValueError: The last name is not in the list

 py example_3.py
Enter your first name: Adam
Enter your last name: Aron
Fname is Adam Lname is Aron

#################################################################

In the example_4.py we added the third args job without define in the __str__() method
running again still work but don't print the job in line 21 see the test:
py example_4.py
Enter your first name: Dill
Enter your last name: Abdulla
Enter your job: Developer
Dill Abdulla


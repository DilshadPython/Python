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
  File "/home/OOProgrammingH/Classes/example_2.py", line 27, in <module>
    main()
  File "/home/OOProgrammingH/Classes/example_2.py", line 14, in main
    user = get_user()
           ^^^^^^^^^^
  File "/home/OOProgrammingH/Classes/example_2.py", line 23, in get_user
    return User(first_name, last_name, age)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/OOProgrammingH/Classes/example_2.py", line 6, in __init__
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
  File "/home/OOProgrammingH/Classes/example_3.py", line 31, in <module>
    main()
  File "/home/OOProgrammingH/Classes/example_3.py", line 18, in main
    user = get_user()
           ^^^^^^^^^^
  File "/home/OOProgrammingH/Classes/example_3.py", line 27, in get_user
    return User(first_name, last_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/OOProgrammingH/Classes/example_3.py", line 8, in __init__
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

################################################################

In example_5.py we create extra methods called my_work() for the third args job
and we printed and called this method in line 32 and 33 but not define in __str__()

Testing:
 py example_5.py
Enter your first name: Dilshad
Enter your last name: Abdulla
Enter your job: Developer

# output
Dilshad Abdulla
Work status
JavaScript

 py example_5.py
Enter your first name: Dilshad
Enter your last name: Abdulla
Enter your job:
~ output
Dilshad Abdulla
Work status
/

################################################################
This is before we create setter and getter method when we run this is the output
py user.py
Enter your full name: Dilshad Abdulla
Enter your city: Cologne
Dilshad Abdulla from Greenwood, London

################################################################

Now we define city() methods twice as setter and getter method user_1.py
which is called property write like  @property() called decorator
To run and show the error before we change everything
py user_1.py
Enter your full name: Dilshad
Enter your city: London
Traceback (most recent call last):
  File "/home/OOProgrammingH/Classes/user_1.py", line 49, in <module>
    main()
  File "/home/OOProgrammingH/Classes/user_1.py", line 36, in main
    user = get_user()
           ^^^^^^^^^^
  File "/home/OOProgrammingH/Classes/user_1.py", line 45, in get_user
    return User(fullname, city)
           ^^^^^^^^^^^^^^^^^^^^
  File "/home/OOProgrammingH/Classes/user_1.py", line 12, in __init__
    self.city = city
    ^^^^^^^^^
  File "/home/OOProgrammingH/Classes/user_1.py", line 31, in city
    raise ValueError("Invalid city which is not in the list")
ValueError: Invalid city which is not in the list

This error is happed because we use self.city in line 37 we have deleted because it is not required
we try one way correct as in the code :
 py user_1.py
Enter your full name: Dilshad
Enter your city: Cologne
Dilshad from Cologne

We try not correctly we still get the error like below:
 py user_1.py
Enter your full name: Dilshad
Enter your city: London
Traceback (most recent call last):
  File "/home/OOProgrammingH/Classes/user_1.py", line 49, in <module>
    main()
  File "/home/OOProgrammingH/Classes/user_1.py", line 36, in main
    user = get_user()
           ^^^^^^^^^^
  File "/home/OOProgrammingH/Classes/user_1.py", line 45, in get_user
    return User(fullname, city)
           ^^^^^^^^^^^^^^^^^^^^
  File "/home/OOProgrammingH/Classes/user_1.py", line 12, in __init__
    self.city = city
    ^^^^^^^^^
  File "/home/OOProgrammingH/Classes/user_1.py", line 31, in city
    raise ValueError("Invalid city which is not in the list")
ValueError: Invalid city which is not in the list

# After we create two getter and setter we will delete both if statement in the __init__ method

try to test:
 py user_2.py
Enter your full name: Dilshad
Enter your city: Cologne
Dilshad from Cologne
/Dev/OOProgrammingH/Classes$ py user_2.py
Enter your full name:
Enter your city: Cologne
Traceback (most recent call last):
  File "/home/OOProgrammingH/Classes/user_2.py", line 61, in <module>
    main()
  File "/home/OOProgrammingH/Classes/user_2.py", line 48, in main
    user = get_user()
           ^^^^^^^^^^
  File "/home/OOProgrammingH/Classes/user_2.py", line 57, in get_user
    return User(fullname, city)
           ^^^^^^^^^^^^^^^^^^^^
  File "/home/OOProgrammingH/Classes/user_2.py", line 9, in __init__
    self.fullname = fullname
    ^^^^^^^^^^^^^
  File "/home/OOProgrammingH/Classes/user_2.py", line 27, in fullname
    raise ValueError("Invalid fullname cannot be empty")
ValueError: Invalid fullname cannot be empty

We delete the if statement after define tw properties method setter and getter for both args and run the code testing
in correct way and wrong ways see the restluts.

################################################################

We have entered the correct name but we will print the line 45
user._city = f"The city {user._city} you entered is not valid"
in the output
py user_3.py
Enter your full name: Dilshad
Enter your city: Cologne

# output
Dilshad from The city Cologne you entered is not valid

But if you enter invalid city name this is what happen:
 py user_3.py
Enter your full name: Dilshad
Enter your city: London
Traceback (most recent call last):
  File "/home/OOProgrammingH/Classes/user_3.py", line 57, in <module>
    main()
  File "/home/OOProgrammingH/Classes/user_3.py", line 44, in main
    user = get_user()
           ^^^^^^^^^^
  File "/home/OOProgrammingH/Classes/user_3.py", line 53, in get_user
    return User(fullname, city)
           ^^^^^^^^^^^^^^^^^^^^
  File "/home/OOProgrammingH/Classes/user_3.py", line 6, in __init__
    self.city = city
    ^^^^^^^^^
  File "/home/OOProgrammingH/Classes/user_3.py", line 39, in city
    raise ValueError("Invalid city which is not in the list")
ValueError: Invalid city which is not in the list


'''
Here we just created class with full empty data and without any methods like
__init__ or __str__ and __repr__. etc ...
The goal here is to understand how to create a class and to make it easy to
work type ... to show class is created and the program is running
'''

class User:
    ...

def main():
    user = get_user()
    print(f"full name is: {user.first_name} {user.last_name}")

def get_user():
    # we create an object from the User class
    user_obj = User()
    user_obj.first_name = input("Enter your first name: ")
    user_obj.last_name = input("Enter your last name: ")
    return user_obj

if __name__ == "__main__":
    main()


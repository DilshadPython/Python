'''
Here we have define the __init__ method which is called initialization of the class
dunder __init__(self) which is instance methods
we define the data we want like first name and last name and age
'''
class User:

    # This is the initialization of the class this method will automatic called by class object
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

def main():
    user = get_user()
    print(f"Full name is: {user.first_name} {user.last_name} {user.age} years old")

def get_user():
    # we create class here with tuple
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = input("Enter your age: ")
    # we created structor here from the User class and adding the tow data in the structor class
    user = User(first_name, last_name, age)
    return user

if __name__ == "__main__":
    main()


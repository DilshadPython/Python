class User:

    # This is the initialization of the class
    def __init__(self, first_name, last_name, age):
        if not first_name and not last_name:
            raise ValueError("First name and last name cannot be empty")
        if first_name not in ['Dill', 'Monika'] and last_name not in ['Abdulla', 'Carter']:
            raise ValueError("The first name and last name are not in the list")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

def main():
    user = get_user()
    print(f"Full name is: {user.first_name} {user.last_name} {user.age} years old")

def get_user():
    # we create data
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = input("Enter your age: ")
    # we created structor here from the User class and adding the tow data in the structor class
    return User(first_name, last_name, age)


if __name__ == "__main__":
    main()


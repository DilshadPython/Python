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


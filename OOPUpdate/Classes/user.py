class User:
    # This is the initialization of the class
    def __init__(self, fullname, city):
        if not fullname:
            raise ValueError("First name cannot be empty")
        if city not in ['Cologne', 'Brentwood']:
            raise ValueError("The city is not in the list")
# we use self to access to the args
        self.fullname = fullname
        self.city = city

# this method will be called as soon we create user = User() and print(user)
    def __str__(self):
        return f"{self.fullname} from {self.city}"

def main():
    user = get_user()
    user.city = "Greenwood, London"
    print(user)

def get_user():
    # we create data
    fullname = input("Enter your full name: ")
    city = input("Enter your city: ")
    # we created structor here from the User class and adding the tow data in the structor class
    return User(fullname, city)


if __name__ == "__main__":
    main()

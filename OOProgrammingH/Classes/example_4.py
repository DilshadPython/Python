class User:
    # This is the initialization of the class, we added job as third args
    def __init__(self, first_name, last_name, job):
        if not first_name:
            raise ValueError("First name cannot be empty")

        if last_name not in ['Aron', 'Abdulla']:
            raise ValueError("The last name is not in the list")

        self.first_name = first_name
        self.last_name = last_name
        self.job = job


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


def main():
    user = get_user()
    print(user)


def get_user():
    # we create data
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    job = input("Enter your job: ")
    # we created structor here from the User class and adding the tow data in the structor class
    return User(first_name, last_name, job)


if __name__ == "__main__":
    main()

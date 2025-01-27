class User:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"This full name is {self.fname} and last name {self.lname}"

    @classmethod
    def get(cls):
        fname = input("Enter your first name: ")
        lname = input("Enter your last name: ")
        return cls(fname, lname)

def main():
    user = User.get()
    print(user)


if __name__ == "__main__":
    main()
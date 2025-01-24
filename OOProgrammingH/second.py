def main():
    name, town = get_user()
    print(f"{name} is live in {town}")

def get_user():
    name = input("What is your name? ")
    town = input("What is your town? ")
    return name, town

if __name__ == "__main__":
    main()
def main():
    name = get_name()
    town = get_town()
    print(f"{name} is live in {town}")

def get_name():
    return input("What is your name? ")

def get_town():
    return input("What is your town? ")

if __name__ == "__main__":
    main()
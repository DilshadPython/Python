def main():
    user = get_user()
    print(f"{user[0]} is live in {user[1]} from {user[2]}.")

def get_user():
    name = input("What is your name? ")
    town = input("What is your town? ")
    country = input("What is your country? ")
    # return a tuple() we can't change the iput
    return (name, town, country)

if __name__ == "__main__":
    main()
def main():
    user = get_user()
    # f we enter the name to Dilmac we will change the return town and country to Bad Berneck and Germany
    if user[0] == 'Dilmac':
        user[1] = 'Bad Berneck'
        user[2] = 'Germany'
    print(f"{user[0]} is live in {user[1]} from {user[2]}.")

def get_user():
    name = input("What is your name? ")
    town = input("What is your town? ")
    country = input("What is your country? ")
    # return a list() we will change the input to Dilmac to see the results
    return [name, town, country]

if __name__ == "__main__":
    main()
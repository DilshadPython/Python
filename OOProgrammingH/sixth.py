def main():
    user = get_user()
    # f we enter the name to Dilmac we will change the return town and country to Bad Berneck and Germany
    if user['name'] == 'Dilmac':
        user['town'] = 'Bad Berneck'
        user['country'] = 'Germany'
    print(f"{user['name']} is live in {user['town']} from {user['country']}.")

def get_user():
    name = input("What is your name? ")
    town = input("What is your town? ")
    country = input("What is your country? ")
    # return a dict() we will change the input to Dilmac to see the results
    return {"name": name, "town": town, "country": country}

if __name__ == "__main__":
    main()
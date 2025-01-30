class User:
    # This is the initialization of the class
    def __init__(self, fullname, city):
        # we use self to access to the args
        self.fullname = fullname
        self.city = city

    # this method will be called as soon we create user = User() and print(user)
    def __str__(self):
        return f"{self.fullname} from {self.city}"

    @property
    def fullname(self):
        return self._fullname
    """
    # we can change the first argo in the method to value like: def fullname(self, value)
    # instead of fullname still work but we have to add _ after the setter method created
    _fullname 
    """
    @fullname.setter
    def fullname(self, fullname):
        if not fullname:
            raise ValueError("Invalid fullname cannot be empty")
        self._fullname = fullname

    # Getter without define any args except self but has to be exactly like in the setter _city
    @property
    def city(self):
        return self._city

    # Setter which is always come with self and second args
    @city.setter
    def city(self, city):
        """
        because we are checking the city name we can't user the city name as defined in the class
        we have to add _ in front of the args will be like _city
        """
        if city not in ['Cologne', 'Brentwood']:
            raise ValueError("Invalid city which is not in the list")
        self._city = city


def main():
    user = get_user()
    user._city = f"The city {user._city} you entered is not valid"
    print(user)

def get_user():
    # we create data
    fullname = input("Enter your full name: ")
    city = input("Enter your city: ")
    # we created structor here from the User class and adding the tow data in the structor class
    return User(fullname, city)


if __name__ == "__main__":
    main()

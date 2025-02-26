# We initialize the name in parent class which is Licence after inherite the child class
# we don't need initialize the name in child class
class Licence:
    def __init__(self, name):
        if not name:
            raise ValueError("Licence name is required")
        self.name = name

    def __str__(self):
        return self.name


class Driver(Licence):
    def __init__(self, name, age):
        # super mean the Licence class here
        super().__init__(name)
        self.age = age

    def __str__(self):
        return super().__str__() + f"\t age: {self.age}"

    ...

class Car(Licence):
    def __init__(self, name, platenumber):
        super().__init__(name)
        self.platenumber = platenumber

    def __str__(self):
        return super().__str__() + f"\t platenumber: {self.platenumber}"

    ...
licence = Licence("Dilshad")
user = Driver("John", 18)
driver = Car("Tomas", 58124588)

print(licence)
print(user)
print(driver)


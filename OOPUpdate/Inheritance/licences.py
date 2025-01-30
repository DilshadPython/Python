# We initialize the name in parent class which is Licence after inherite the child class
# we don't need initialize the name in child class
class Licence:
    def __init__(self, name):
        if not name:
            raise ValueError("Licence name is required")
        self.name = name


class Driver(Licence):
    def __init__(self, name, age):
        # super mean the Licence class here
        super().__init__(name)
        self.age = age

    ...

class Car(Licence):
    def __init__(self, name, platenumber):
        super().__init__(name)
        self.platenumber = platenumber

    ...
licence = Licence("Dilshad")
user = Driver("John", 18)
driver = Car("Tomas", 58124588)


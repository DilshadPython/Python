class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Wizard name is required")
        self.name = name


class User(Wizard):
    def __init__(self, name, age):
        # super mean the Wizard class here
        super().__init__(name)
        self.age = age

    ...

class Driver(Wizard):
    def __init__(self, name, driving_number):
        super().__init__(name)
        self.driving_number = driving_number

    ...
wizard = Wizard("Dilshad")
user = User("John", 18)
driver = Driver("Tomas", 58124588)
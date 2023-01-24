Encapsulation:

Encapsulation: The first of the three pillars of OOP
Encapsulation refers to the safe storage of data (as attributes)

Data should be accesses only through instance methods
Data should be validated as correct (depending on the requirements set in class methods)
Data should be safe from changes by external processes.

- Although normally set in a setter method, instance attribute values can be set anywhere
- Encapsulation in Python is a voluntary restriction 
- Python does not implement data hiding, as does another languages

In summary, class attributes remain the same for every object and are defined outside the __init__() function. Instance attributes are some what dynamic because they can have different values in each object.

Encapsulation is instance attributes 

# self is an instance of Room self is instance of which methods will be called
class Room:
    def clean(self):
        print('clean the room')


# Description of Encapsulation
class Encapsulation:

    # define the argument in the setter method
    def setter_method(self, name):
        self.name = name
    
    # return the argument is given from setter method
    def getter_method(self):
        return self.name
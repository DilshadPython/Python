from collections import namedtuple


'''
Here you can't specify the type of the data in the namedtuple or define the 
type of the variables.
'''
University = namedtuple('University', ['name', 'city', 'year'])

obj = University('Anglia Rusking University', 'Chelmsford', '1987')

print(obj)

print('\n####################################################\n')

from dataclasses import dataclass

'''
The reason of adding @dataclass to allow you specify all types of you data
'''


@dataclass
class Student:
    name: str
    points: float
    year_graduate: int
    is_passed: bool = True  # use as default True

    @property
    def info(self):
        return f'{self.name} graduate in {self.year_graduate} his market was {self.points} and he passed {self.is_passed}'


# create an object
std_obj = Student('Tom Adam', 67.5, 2018, True)

print(std_obj)
print(std_obj.name, std_obj.points, std_obj.year_graduate, std_obj.is_passed)


print('\n')

'''
Because use property decorator on this method you have call the info method without
prantecy, but if you remove the property decorator you have to call with prantecy 
std_obj.info()
'''
print(std_obj.info)

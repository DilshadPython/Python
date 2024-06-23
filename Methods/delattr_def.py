class Person:
  name = "John"
  age = 36
  country = "Norway"

obj = Person()

#Before
print('The class data: ', obj.name, ' | ', obj.age, ' | ', obj.country)

#After delete all class data contents
delattr(Person, 'age')

# The Person object will no longer contain an "age" property
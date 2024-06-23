class Items:
    name = "Glasses"
    number = 36
    made = "Germany"

obj = Items()

#Before
print('The class data: ', obj.name, ' | ', obj.number, ' | ', obj.made)

#After delete all class data contents
delattr(Items, 'number')

# The Person object will no longer contain an "age" property

print(obj.name, ' | ', obj.made)
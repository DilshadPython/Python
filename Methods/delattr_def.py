class Items:
    name = "Glasses"
    number = 36
    made = "Germany"

obj = Items()

#Before
print('The class data: ', obj.name, ' | ', obj.number, ' | ', obj.made)

# check before delete
item_number = hasattr(Items, 'number')
print(item_number)

#After delete all class data contents
delattr(Items, 'number')

# The Person object will no longer contain an "age" property

print(obj.name, ' | ', obj.made)

# Check after deleted
item_number_after = hasattr(Items, 'number')
print(item_number_after)
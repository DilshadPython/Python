# class variables or class attribute and instance attribute
# Important to understand how class attribute and instance attribute works
class Language:
    # class veriable
    class_name = 'Python'


obj = Language()
# calling call variable name we are reading it
print('\nCalling class attribute: ', obj.class_name)

# Now we set the name to JavaScript and become instance vairable or attribute
obj.class_name = 'Javascript'
print('\nCalling instance attribute: ', obj.class_name)

# next we delete the class_name which is select the instance attribute not class attribute

del obj.class_name
print('\nWe have deleted the instance attribut here. ', obj.class_name)
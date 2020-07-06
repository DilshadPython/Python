class Student:
    '''
    Instance method
    Can modify object instance state
    Can modify class state
    '''

    def instance_method(self):
        return 'Instance method has been called', self

    '''
	Class method
	x Can't modify object instance state
	Can modify class state
	class method Only access class itself, the object represent the class
	it is not be able to access self object instance method above
    '''
    @classmethod
    def cls_method(cls):
        return 'Class method has been calles', cls

    '''
	Static method
	x Can't modify object instance state 
	x Can't modify class state
	This method does not has any argument like self, or cls and not be 
	able to access self object and cls object in instance method or class
	method.
    '''
    @staticmethod
    def static_method():
        return 'Static method has been called'

# create an object 
obj = Student()

# we call from this object to instance class and see the result
print(obj.instance_method())
'''
output:
access to the class itself __main__.Student and 
the object of this class (0x7fae147082e0)
('Instance method has been called', <__main__.Student object at 0x7fae147082e0>)
'''
print(obj.cls_method())
'''
output:
In class method has only access to the class itself__main__..Student
but not access to any object as you see the output
('Class method has been calles', <class '__main__.Student'>)

'''
print(obj.static_method())
'''
output:
it calls the method only as you:
Static method has been called 
'''

########################################################################
# Now we call from the class each methods one by one and see the output:

print(Student.cls_method())
'''
clling class method from class itself:
('Class method has been calles', <class '__main__.Student'>)
'''

print(Student.static_method())
'''
calling static method from class itself the output:
Static method has been called
'''
print(Student.instance_method())
'''
call instance method from class itself it doesnt work !!!
Traceback (most recent call last):
  File "explain_instance_class_static_method.py", line 73, in <module>
    print(Student.instance_method())
TypeError: instance_method() missing 1 required positional argument: 'self'
'''
# Very important if we put the obj as an argument in the instance_method
# like below it works like obj.instance-method() 
# print(Student.instance_method(obj))
# Output of line 84:
# ('Instance method has been called', <__main__.Student object at 0x7f08eda2b2e0>)

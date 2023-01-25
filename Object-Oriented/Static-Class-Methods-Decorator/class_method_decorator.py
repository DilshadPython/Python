'''
This is shows how the class methods work
A clas method takes the class not instance as argument and
works with class object (Class method is bound method)
'''


class InstanceCounter(object):
    """docstring for InstanceCount"""
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, new_val):
        self.val = new_val

    '''
    This is the static method
    '''
    def get_val(self):
        return self.val

    '''
    This is the class method to explain better is to change self to cls
    and to make it works need to add on the top of the method @classmethod 
    to avoid error with cls it's exactly the same like instance method but
    it will explain better called bound method. or Class method
    '''
    @classmethod
    def get_count(cls):
        return cls.count


a = InstanceCounter(107)
b = InstanceCounter(22)
c = InstanceCounter(81)

for obj in (a, b, c):
    print('Val of obj %s' % (obj.get_val()))
    print('Count : %s' % (obj.get_count()))

print('=========')
''' We will call the class method only '''
print(InstanceCounter.get_count())
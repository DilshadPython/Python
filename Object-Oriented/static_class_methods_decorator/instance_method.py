'''
This is shows how the instance methods work
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
    This is the class method
    '''

    def get_count(self):
        return InstanceCounter.count


a = InstanceCounter(107)
b = InstanceCounter(22)
c = InstanceCounter(81)

for obj in (a, b, c):
    print('Val of obj %s' % (obj.get_val()))
    print('Count : %s' % (obj.get_count()))

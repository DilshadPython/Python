'''
Etarator means you are repeating some elements in your list you have created one 
by one
'''


class Alphabetices():

    def __init__(self):
        self.char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                     'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
        # default
        self.index = -1

    # define iterator method
    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1

        if self.index == len(self.char):
            raise StopIteration(" End of the list string")
        return self.char[self.index]

# create an object
obj = Alphabetices()

myiter = iter(obj)

print(myiter)
print('=============================================================')
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print('=============================================================')
for itr in myiter:
    print(itr)
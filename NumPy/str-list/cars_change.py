import numpy as np

a = np.array([['BMW', 'AUDI',
               'FORD', 'OPEL',
               'TOYOTA', 'NISSAN',
               'PORSHE', 'MERCEDES',
               'VOLXWAGEN'],
              ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']])

# Before 
print(a)
# we change all elemt in index to XX
a[:, 3] = 'XX'
# after
print(a)

a[1, :] = 'None'
# change all elements in second list to None
print(a)
# here we change all cars name to 0
a[0, :] = '0'
print(a)

#
a[:, 3] = [2, 2]
print(a)
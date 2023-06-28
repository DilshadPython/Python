import numpy as np

a = np.array([['BMW', 'AUDI',
               'FORD', 'OPEL',
               'TOYOTA', 'NISSAN',
               'PORSHE', 'MERCEDES',
               'VOLXWAGEN'],
              ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']])

# here displat specific indexing
# [start, end, stepsize]
# its second list which is 1, element 2 is C, ended 7 which is H
# step by 2 
print(a[1, 1:7:2])
# first list
print(a[0, 1:8:2])

# change an element in the list
a[1, 4] = 'Element'
print(a[1, 4])
print(a[1:])

# here we change the Ople to Volovo and show up to index 7 which is PORSHE
a[0, 3] = 'VOLVO'
print(a[0, :7])
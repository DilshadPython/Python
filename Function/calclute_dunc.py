import math

''' Create function do some calculation or cercle '''
print('We will looking for pi function in math module')
print(dir(math))

print('The pi value is :', math.pi)

print('')


def cycling(raidus):
    ''' We calculate raudis of cerciler '''
    valume = 4.0 / 3.0 * math.pi * raidus**3
    return valume

print(cycling(5))

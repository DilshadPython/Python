import math


a = math.acos(0.72)
b = math.acos(-0.72)

print('The value of acos(0.72) : ', a, 'Radians')
print('The value of acos(-0.72) : ', b, 'Radians')

# pi = 3.14159265
result = math.acos(0.72) * (144.0 / math.pi)
print('The value of acos(0.72) : ', result, 'Degrees')
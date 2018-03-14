import random

import string

color = ['white', 'blue', 'orange']

for x in range(10):
	print(random.choice(color))


print()
test = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(1, 9)])

print(test)
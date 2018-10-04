import random 


for x in range(10):
	print(random.uniform(3, 8))

print()

for x in range(10):
	print(random.normalvariate(0, 0.35))

print()
for x in range(30):
	print(random.randint(1, 6))
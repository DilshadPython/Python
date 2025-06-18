import random

my_id_num = [
	num for num in range(18) if num > 0
]

print(random.choices(my_id_num))


numbers = [random.randint(1, 16) for _ in range(10)]

print(set(numbers)) # remove duplication
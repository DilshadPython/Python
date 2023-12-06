import random

my_id_num = [
	num for num in range(18) if num > 0
]

print(random.choices(my_id_num))


numbers = [random.randint(1, 16) for _ in set(range(8))]
non_duplicate = [set(numbers) for number in range(1)]
print(non_duplicate)

print(numbers, ' > Numbers')
a = [1, 2, 3, 4, 6, 7, 8, 33, 6, 9, 98, 22, 12, 23]

if (n := len(a)) > 10:
	print(f"List is too long ({n} elements, expected <= 10)")

## output
# >>> List is too long (14 elements, expected <= 10)

print('##########################\n')
b = [6, 7, 8, 33, 6, 9, 98, 22, 12]

if (m := len(b)) < 10:
	print(f"List is too short ({m} elements, expected >= 10)")
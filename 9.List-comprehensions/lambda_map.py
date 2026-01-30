print()
numbers = [1, 3, 5, 7, 9, 11]
print(numbers)

print()
new_list = list(map(lambda x: x * 2, numbers))
print(new_list)

print()

# print mod numbers
a_list = list(map(lambda x: x * x, numbers))
print(a_list)

print()

# display even number
b_list = [x for x in range(30) if x % 2 == 0]
print(b_list)

print()

# use filter
c_list = list(filter(lambda x: x % 2 == 0, range(20)))
print(c_list)

print()

d_list = list((letter, x) for letter in 'AbCdE' for x in range(3))
print(d_list)

print()

e_list = [(letter, x) for letter in 'AbCdE' for x in range(2)]
print(e_list)
vector = [2, 9, 4, -6, 1, 5.1, -7.9]

# we want to multiply 6 to each value in the list

multiply = [4 * x for x in vector]

print(multiply)

print()

# Cartesian Product
'''
a = {1, 2}
b = {i, j}

a*b = {(1,i), (1, j), (2, i), (2, j)}
'''

A = [2, 4, 6, 8, 10]
B = [1, 3, 5, 7, 9]

cart_pro = [(a, b) for a in A for b in B]

print(cart_pro)

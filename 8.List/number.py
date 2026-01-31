num_lst = [6, 9, 2, 3, 5, 7, 4, 10, 1, 8]

print()
lst_a = sorted(num_lst)

print('\t sorted: ', lst_a)
print()
print('\t original: ', num_lst)

print()
num_lst.sort()
print('\t sorted by num_lst.sort() ', num_lst)

print()
lst_b = sorted(num_lst, reverse=True)
print('\t reversed this way reverse=True ', lst_b)

print()
num_lst.sort(reverse=True)
print('\t reversed use sort(reverse=True) ', num_lst)

# This is tuple
tup_num = (6, 9, 2, 3, 5, 7, 4, 10, 1, 8)

print()
# We sort it to the list
lst_c = sorted(tup_num)
print('\t sorted Tuple: ', lst_c)

dic = {'name': 'Tom', 'age': 35, 'city': 'New York'}
print()

lst_d = sorted(dic)
print('\t sorted Dictionary: ', lst_d)

print()
abs_lst = [1, -4, -3, 5, -2, -1, 3, 2]

print()
print('\t: ', abs_lst)
print()

# sorted by absolute value
lst_abs = sorted(abs_lst, key=abs)
print('\t sorted: ', lst_abs)
print()
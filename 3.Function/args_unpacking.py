
def unpacking_func(a, b, c):
    print(a, b, c)

tuple_vec = (1, 0, 1)
dict_vec = {'a': 1, 'b': 0, 'c': 1}
list_vec = [2, 0, 2]

print('Tuple')
unpacking_func(*tuple_vec)
print('')
print('Dictionary')
unpacking_func(*dict_vec)
print('')
print('List ')
unpacking_func(*list_vec)
print('')
print('Using double astrikes only in dict')
unpacking_func(**dict_vec)


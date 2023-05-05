
def unpacking_func(a, b, c):
    print(a, b, c)

tuple_vec = (1, 0, 1)
dict_vec = {'a': 1, 'b': 0, 'c': 1}

unpacking_func(*tuple_vec)
print('')
unpacking_func(*dict_vec)
print('')
unpacking_func(**dict_vec)

numbers = [2, 3, 5, 7, 1, 8]

def gen_func(numbers = [2, 3, 5, 7, 1, 8]
):
    for x in numbers:
        yield x * x

create_gen = gen_func(numbers)
for x in create_gen:
    print(x)
print('\n=====')
# use comprehenesion
new_gen = (x * x for x in range(10))
for a in new_gen:
    print(a)


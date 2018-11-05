def fibonaci_generator(number):
    a, b = 0, 1

    for x in range(0, number):
        yield('{} {}'.format(x + 1, a))
        a, b = b, a + b

for item in fibonaci_generator(300):
    print(item)

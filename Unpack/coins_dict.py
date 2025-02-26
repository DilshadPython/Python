def total(length, width, height):
    # we enter cm and convert to inch
    return (length * width * height) * 0.393701

# we put the valuse of each as dict
coins = {'length': 15, 'width': 10, 'height': 8}
print(total(coins['length'], coins['width'], coins['height']), 'Inch')

# we can use ** in dictionary instead of *
print('\n We use ** for dictionary')
print(total(**coins), 'Inch')
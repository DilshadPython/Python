def total(length, width, height):
    # we enter cm and convert to inch
    return (length * width * height ) * 0.393701

coins = [75, 40, 25]

# if we use this way it display an error list of length only which is an error
print(total(coins), 'Inch')
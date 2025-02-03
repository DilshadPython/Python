def total(length, width, height):
    # we enter cm and convert to inch
    return (length * width * height ) * 0.393701

coins = [75, 40, 25]
print(total(coins[0], coins[1], coins[2]), 'Inch')

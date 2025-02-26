# Using here unpacking to fix the coins list
def total(length, width, height):
    # we enter cm and convert to inch
    return (length * width * height ) * 0.393701

coins = [75, 40, 25]
# We use * in front of *coins to unpack the list and make it work
print(total(*coins), 'Inch')
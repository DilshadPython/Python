def total(length, width, height):
    # we enter cm and convert to inch
    return (length * width * height ) * 0.393701

print(total(75, 45, 30), 'Inch')
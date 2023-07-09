print('Enter a float numbers')
x = float(input('Enter the x: '))
y = float(input('Enter the y: '))

result = round(x + y)
# , is optional
# round(number[, ndigits])
print('Result: ', result)

# Enter the x: 22.56
# Enter the y: 15.09
# 38
z = round(x + y)
print('Z: ', f"{z:,}")

total = round(float(input('Enter the a: ')) + float(input('Enter the b: ')))
print('Total: ', total)
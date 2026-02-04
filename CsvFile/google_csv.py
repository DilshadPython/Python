
datas = open('csv/google_stock_data.csv', 'r')

# for data in datas:
# 	print(data)

lines = [line for line in open('csv/google_stock_data.csv')]

print(lines[0])
print()
print(lines[1])
# use strip() to remove empty space and split used to divid the string to sapert string seperate by (,)
# strip().split(',') put in the string with duble '')

print(lines[0].strip().split(','))

datas = [line.strip().split(',') for line in open('csv/google_stock_data.csv')]
print()
print(' We use list competences but we test two lines for test:')
print(datas[0])
print(datas[1])

print()
print('The result display all string correct but we have a number must be int or float not str!')

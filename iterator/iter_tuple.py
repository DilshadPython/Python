square = ((21, 6), (7, 12), (22, 31), (44, 22))

for points in square:
	print(points)

print('============')

sqitr = iter(square)
print(next(sqitr))
print(next(sqitr))
print(next(sqitr))
print(next(sqitr))
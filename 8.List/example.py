a = [19, 2, 3, 17, 5, 6, 15, 8, 9, 10, 99, 12]

b = []

for x in a:
    if len(list(a)) == 1:
        break
    else:
        b += [a.pop(0)]

print(a)
print(b)

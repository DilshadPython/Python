file = open('grades.txt')

listcomp = [x for x in file]
# if we run the file here this is the outout
# ['23\n', '45\n', '76\n', '34\n', '56\n', '98\n', '100\n', '30\n', '61\n', '77\n', '17']
print(listcomp)

print('=====================================================')
file = open('numbers.txt')
# rstrip() --> remove \n
comp = [x.rstrip() for x in file]

print(comp)

'''
reading files
open function and mode means read or write
file_open = open(filename, mode)
'''

file_open = open('emailList.txt', 'r+')
for mail in file_open:
	print(mail)
file_open.close()

print('========================\n')
my_file = open('emailList.txt')
count = 0
for line in my_file:
	count = count + 1
print('Number of line: ', count)
my_file.close()

print('========================\n')
new_version = open('emailList.txt')
read_me = new_version.read()
print(read_me)
print(len(read_me))
print('=============')
print(read_me[:50])
new_version.close()
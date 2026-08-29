import os


print()
print(os.getcwd())

print()
# find the environ file in my python path
# /home/azad/Devel/Python
file_path = os.environ.get('/home/azad/Devel/Python/python-doc.txt')
# print(os.environ.get('/home/azad/Devel/Python/'))
print(file_path)

print()
# display the path dir or the file name not exists
print(os.path.basename('/dilshad/textme.txt'))
print()
print(os.path.dirname('/dilshad/textme.txt'))

print()
# to check is the file or path are exists
print(os.path.exists('/dilshad/textme.txt'))

print()
# split the filename with the extension format
print(os.path.splitext('/dilshad/textme.txt'))
print()

# split the filename with the extension format
print(os.path.splitext('/dilshad/textme.rst'))
print()

# split the filename with the extension format
print(os.path.splitdrive('/dilshad/textme.txt'))
print()

# display the root path
print(os.path.splitroot('/dilshad/textme.txt'))
print()

# display all command exists in path methods
for filename in dir(os.path):
    print(filename)

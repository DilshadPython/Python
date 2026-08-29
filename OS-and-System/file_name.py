import os

print(os.getcwd())
# create new txt file
# os.stat('myfile.txt')

new_file = open('newfile.txt','w')
new_file.close()

# change the name of the file we created before
os.rename('newfile.txt','update_test.txt')

# now we check the date of the file is created
from datetime import datetime

print()
date_file = os.stat('update_test.txt').st_mtime
print(datetime.fromtimestamp(date_file))

print()
# now we find all path and directory name with filename using os.walk() need three different
# names which are dirpath, dirnames and filenames,
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path :',  dirpath)
    print('Directories :',  dirnames)
    print('Files :',  filenames)

print()
print(os.listdir())
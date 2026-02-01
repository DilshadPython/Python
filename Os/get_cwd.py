import os

# Define current directory
print(os.getcwd())

## we change the current directory to another example to main python dir
os.chdir("/home/azad/Devel/Python/")

# now we move to main directory
print(os.getcwd())

# now we try to show all files in mian dir
print(os.listdir()) # > python-dir.list

# we return to current dir pr path
os.chdir("/home/azad/Devel/Python/Os")
# create directory in current path
if os.path.exists('NewDir'):
    # we removed or delete to be able to create newDir
    os.rmdir('NewDir')
else:
    os.mkdir('NewDir')

# create sub dir inside NewDir2, but if the dir is exists? removed and create a new one
if os.path.exists('NewDir2/SubDir'):
    os.removedirs('NewDir2/SubDir')
else:
    # now return to current path or do nothing
    os.makedirs('NewDir2/SubDir')


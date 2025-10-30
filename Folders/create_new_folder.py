import os, errno

try:
    os.makedirs('SecondFolder')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

print("Second Folder created successfully.")
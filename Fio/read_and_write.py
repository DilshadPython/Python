'''
we open the file which is existed cities.txt to read
next open create a copy from the first file we opened to read
doing a loop all read file and wrote to the new file we create a copy
'''
with open('cities.txt', 'r') as rf:
    with open('cities_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
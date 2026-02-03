# to read and create an image file we must use 'rb' and 'wb'

with open('dill.jpg', 'rb') as rf:
    with open('dill_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)
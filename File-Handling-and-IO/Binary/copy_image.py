# to read and create an image file we must use 'rb' and 'wb'

with open('dill.jpg', 'rb') as rf:
    with open('dill_new.jpg', 'wb') as wf:
        img_size = 4096
        rf_img = rf.read(img_size)
        while len(rf_img) < 0:
            wf.write(rf_img)
            rf_img = rf.read(img_size)

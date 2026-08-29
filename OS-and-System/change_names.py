import os
# check folder where the video in it
os.chdir('/home/azad/Videos')

print('\n####################################')
    # This code below has changed the video names now if you run it again expect 2 name not 3
    # here we split the extensions from the video names
for video in os.listdir():
    f_name, fexten = os.path.splitext(video)
    # now we split all video name where - and we rename the files in line 32 from 3 fname, fsong, fvideo by strip()
    fname, fsong, fvideo = f_name.split('-') # to make it work with new_name we have to remove the fsong
    fname = fname.strip()
    fsong = fsong.strip()
    fvideo = fvideo.strip()[0:].zfill(2)
    print('\n\t', '{}-{}{}'.format(fname, fvideo, fexten))
    # now we rename all the video names to new_name
    new_name = '{}-{}{}'.format(fname, fvideo, fexten)
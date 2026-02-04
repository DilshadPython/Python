import os
# check folder where the video in it
os.chdir('/home/azad/Videos')

for video in os.listdir():
    f_name, fexten = os.path.splitext(video)
    fname, fvideo = f_name.split('-')
    print('\n\t', '{}-{}{}'.format(fname, fvideo, fexten))

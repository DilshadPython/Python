import os
# check folder where the video in it
os.chdir('/home/azad/Videos')

# use for loop to search the videos and display in the shell
for video in os.listdir():
    print('\n\t: ', video)

print('\n==================================')

    # here we split the extensions from the video names
for video in os.listdir():
    print('\n\t: ', os.path.splitext(video))
    # we will split the name of the video with extensions
    f_name, f_exten = os.path.splitext(video)
    print('\n\t: ', f_name, '||', f_exten)

print('\n************************************')

    # here we split the extensions from the video names
for video in os.listdir():
    print('\n\t: ', os.path.splitext(video))
    # now we split all video name where -
    print('\n\t:', f_name.split('-'))


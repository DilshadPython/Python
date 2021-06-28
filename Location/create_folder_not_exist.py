import os

# running mkdir again with the same name raises FileExistsError, run this instead:
if not os.path.isdir("New-folder"):
     os.mkdir("New-folder")
else:
     print('This folder already exisit, try another new folder')
from zipfile import *


def create_zipf():
    name_thefile = 'hello.zip'

    writing_obj = ZipFile(name_thefile, 'w')

    # when you create the file you need to close it
    writing_obj.close()

create_zipf()

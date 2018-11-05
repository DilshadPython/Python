import os
from contextlib import contextmanager

current_directory = os.getcwd()
# chdir stand for changing directory
os.chdir('dir-first')

print(os.listdir())
os.chdir(current_directory)

current_directory = os.getcwd()
os.chdir('dir-second')

print(os.listdir())
os.chdir(current_directory)


@contextmanager
def change_dir(location):
    try:
        current_directory = os.getcwd()
        # chdir stand for changing directory
        os.chdir(location)

        yield
    finally:
        os.chdir(current_directory)

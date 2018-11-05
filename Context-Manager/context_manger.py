
# use contextmanager as decorator to docorate a gentertor function
from contexlib import contextmanager


class OpenTextFile():

    # filename, mode if used for open to write and readingin the file
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)

        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self. file.close()

# if you use with function you don't need to close the file
with OpenTextFile('myfile.txt', 'w') as file:
    file.write('Add some message to the file')

# to make sure that the file is close run the print line
print(file.closed)

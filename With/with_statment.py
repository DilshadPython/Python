# Using with statment to open the Git file to read
# a simple file writer object
  
class MessageWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name
      
    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file
  
    def __exit__(self):
        self.file.close()
  
# using with statement with MessageWriter

with open('withfiled.txt', 'w') as file:
	file.write('# with EXPRESSION as TARGET: SUITE')


import random

import StringIO

class WriteStuff:

	def __init__(self, writer):
		self.writer = writer

	def write(self):
		write_txt = 'This is the message we write.'
		self.writer.write(write_txt)

file_h = open('test.txt')
write_msg = WriteStuff(file_h)
write_msg.write()
file_h.close()

str_h = StringIO.StringIO()
write_msg1 = WriteStuff(str_h)
write_msg1.write()

print('\nFile object: ', open('test.txt', 'r').read())
print('\bStrindIO object: ', str_h.get_val())

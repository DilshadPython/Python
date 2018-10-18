from zipfile import *

def add_data_to_zipf():
	name_thefile = 'hello.zip'

	''' here we write the data we want to add to the file (in create_zipfile)
		we already created the zip file now we add the data in the zip file
	'''
	data_list = ['Goland', 'JavaScript', 'Bootstrap', 'DevOp', 'CpluPlus',
				 'Angular', 'Djnago', 'Flask', 'AWS']

	file_obj = ZipFile(name_thefile, 'w')

	# we add some message to each data has been added to zip file
	for msg in data_list:
		# we will make all the data to ended with .py 
		name_obj = msg + '.py'
		handle_obj = open(name_obj, 'w')
		handle_obj.write(' I love python programming more than ' + msg.upper())
		
		# now we need to closed
		handle_obj.close()

		# here we adding all the data_list to zip file
		file_obj.write(name_obj)

	# when you create the file you need to close it
	file_obj.close()

add_data_to_zipf()

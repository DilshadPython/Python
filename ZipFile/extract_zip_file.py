from zipfile import *

def extract_zipf():
	name_thefile = 'hello.zip'

	file_obj = ZipFile(name_thefile, 'r')

	# we will check the list of data in the zip file using infolist() function
	for files in file_obj.infolist():
		print(files)

	# we read the data names using namelist() function in the zip file
	for file_name in file_obj.namelist():
		print(file_name)

	# we extract one file to the new_folder from zip file
	file_obj.extract('Goland.py', 'new_folder')

	# we extract all file to forlder_forall
	file_obj.extractall('folder_forall')

	# when you create the file you need to close it
	file_obj.close()

extract_zipf()

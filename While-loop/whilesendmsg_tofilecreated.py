# we create a file where put the data

create_file = open("news.txt", 'w')
msg = None
print('If you want quit enter q or, Please enter a word or any message or number:')
msg = input()
# now we sending message to file news.txt created above using whileloop
while msg != 'q':
	# we send the message before the input because avoid q to be entered to the file
	# if we put after input() in this case the q also send to file
	create_file.write('You entered > ' + msg + '\n')
	print('If you want quit enter q or, Please enter a word or any message or number:')
	msg = input()

create_file.close()
# when we runing the file without any extra codes the file is created and sending
# the above messages to the file. When every times you run the file again clear the
# all old msg and enter the new msg you enter
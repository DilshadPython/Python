# we create a file where put the data

create_file_out = open("msg.txt", 'w')
# now we sending text to file msg.txt
create_file_out.write('Welcome to Python\n')
create_file_out.write('Welcome to C++\n')
create_file_out.write('Welcome to Google\n')
create_file_out.write('Welcome to Apple\n')
create_file_out.write('Welcome to Java\n')
create_file_out.write('Welcome to the end.\n')
# we are closing the file here and saved automatic
create_file_out.close()
# when we runing the file without any extra codes the file is created and sending
# the above messages to the file.
file = open('emailList.txt')

for mail in file:
	if mail.startswith('Nicholas.herriot@gmail.com'):
		print(mail, '\n')
	else:
		print('The email not match')
file.close()

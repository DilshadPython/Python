file_v = open('email_from.txt')

for mail in file_v:
	mail = mail.rstrip()
	if mail.startswith('Fron: ') :
		print(mail)
file_v.close()

file_v2 = open('email_from.txt')

print('==========================')
for mail in file_v2:
	mail = mail.rstrip()
	if not mail.startswith('Fron: '):
		continue
	print(mail)

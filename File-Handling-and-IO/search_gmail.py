file_v = open('email_from.txt')

for mail in file_v:
    mail = mail.rstrip()
    if not '@gmail.com' in mail:
    	continue
    print(mail)

file_v.close()

print('=========================')
file_v1 = open('email_from.txt')

for mail in file_v1:
    # mail = mail.rstrip()
    if not '@gmail.com' in mail:
    	print('Display all emails except not gmail.')
    	print(mail)

file_v1.close()


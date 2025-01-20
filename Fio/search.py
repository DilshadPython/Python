file_v = open('email_from.txt')

for mail in file_v:
    mail = mail.rstrip()
    if mail.startswith('From: '):
        print(mail)
file_v.close()

file_v1 = open('email_from.txt')

print('==========================\n')
for mail in file_v1:
    mail = mail.rstrip()   # the rstrip() skipe the if statment
    if not mail.startswith('From:'):
        continue
    print(mail)
file_v1.close()


print('**************************\n')
file_v2 = open('email_from.txt')
for mail in file_v2:
    # mail = mail.rstrip()
    if not mail.startswith('From: '):
    	# continue
    	print(mail)
file_v2.close()

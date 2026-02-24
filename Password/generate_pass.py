import random
import string
import datetime

lower_char = 'abcdefghijklmnopqrstuvwxyz'
upper_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
symbole = '!"£$%^&*()-_=+~#@?\\<>/[]}{'
mix_together = lower_char + upper_char + num + symbole

length = int(input('Enter length of password: '))

password = ''.join(random.sample(mix_together, length))

print('Enter new password: ', password)
f = open("gmail.txt", "a")
x = datetime.datetime.now()
f.write('\n')
f.write(str(x))
f.write(': ')
f.write(password)

f.close()

# You can contact on this number +34 91 514 0000
# Customerqueries@ryanair.com
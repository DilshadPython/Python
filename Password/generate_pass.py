import random
import string

lower_char = 'abcdefghijklmnopqrstuvwxyz'
upper_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
symbole = '!"£$%^&*()-_=+~#@?\\<>/[]}{'
all_together = lower_char + upper_char + num + symbole

length = 16

password = ''.join(random.sample(all_together, length))

print('Enter new password: ', password)

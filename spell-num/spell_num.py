# How to spelling number using inflect

# pip3 install inflect # (VN)
# sudo apt-get install python-inflect  # in the terminal

import inflect

num1 = 6736743
num2 = 21451873

e = inflect.engine()

print(e.number_to_words(num1))
print('\n ======== ')
print(e.number_to_words(num2))

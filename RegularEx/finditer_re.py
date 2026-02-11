'''

'''
import re

text_to_find = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
123 456 7890
888.764.989
532-658-001

Hi Haliluia

. ^ $ ! £ % & * ( ) + = - # ~ @ $ 

teach-cloud.net

Mr Smith
Mrs Trump
Ms Claudia
Miss Georgina

'''

line = 'Parking tickets and enforcement. Parking fines and penalty charge notices PCNs'

# words = input('Enter words: ')
# pattern = re.compile(r'teach-cloud\.net')
# pattern = re.compile(r'\Dt')
pattern = re.compile(r'\W')
# pattern = re.compile(r'\d\d\d')
pattern = re.compile(r'\d\d\d.\d\d\d')

matches = pattern.finditer(text_to_find)

# for match in matches:
#     print('\n\t', match)


with open('data/REeX.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

    matches = pattern.finditer(contents)

    for match in matches:
        print('\n\t', match)

# to test
# print('\n\t', text_to_find[28:31])
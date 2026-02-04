import random

langs = ['Java', 'Python', 'Ruby', 'PHP', 'C++', 'Javascript']

value = random.choice(langs)
print('\n\t -', value, 'Language')

colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'white']

results = random.choices(colors, k=5)
print('\n\t -', results)

results = random.choices(colors, weights=[15, 25, 19, 12, 20, 12], k=5)
print('\n\t -', results)
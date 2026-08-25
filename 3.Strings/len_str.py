name = 'Adam as string'

print(len(name))

print('\n=======')

text = 'The gap between writing basic Python code and developing professional-grade systems is far wider than most devs realize.'
print(len(text))

print('\n=======')
print('professional-grade ' in text)

print('\n=======')
if 'professional-grade ' in text:
    print("Yes, 'professional-grade' is in text")

print('\n=======')
print('Java' not in text)
if 'Java' not in text:
    print("Yes, 'Java' is not in text")
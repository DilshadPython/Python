text = 'The gap between writing basic Python code and developing professional-grade systems is far wider than most devs realize.'

print('Read from beginning until character number 25.\n')
print(text[:25])

print('==========\n')
print('Read the last 20 character in the text.\n')
print(text[-20:])

print('==========\n')
print('Remove the last 15 character in the text.\n')
print(text[:-15])

print('==========\n')
print('Ready from character 11 until character 45 from beginning of the line in the text.\n')
print(text[11:-45])

print('==========\n')
print('Ready from the end of line character 45 until character 11 from the end of the line in the text.\n')
print(text[-45:-11])
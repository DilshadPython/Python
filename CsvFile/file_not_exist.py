
try:
	with open('file_not_exisit.txt') as f:
		text = f.read()
except FileNotFoundError:
	text = None 

print(text)
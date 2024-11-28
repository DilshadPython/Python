# print('objects', sep=' ', end='\n'', file=sys.stdout, flash=False)
name = input('Please enter your full name. ').strip().title()

fname, lname = name.split(' ')

print(f'Hey, {name}\n')

print(f"Hi, {fname}\n")

print(f"Hi, {lname}\n")

print(f"Hello, {fname} {lname}")

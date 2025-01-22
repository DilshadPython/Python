name = input('Please enter your full name. ')

# remove all empty or whitespace around the message
name = name.strip()
name = name.title()

print('Hi, {name}')

print(f"Hi, {name}")

print('===============================')

name = name.strip().title()

print(f"Hi, {name}")

# end stop new line
print(f"Hi, {name}", end=' << ')

print('Azad', ' ', end='')
print('Tome')
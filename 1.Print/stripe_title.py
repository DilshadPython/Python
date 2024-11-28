name = input('Please enter your full name. ').strip().title()

print(f"Hi, {name}")
print()

#  stript() Remove whitespace from string and title() set the first character to uppercase
name = name.strip().title()
print(f'Hello, {name}')

name = name.count(name)

print(f"Hi, {name}")

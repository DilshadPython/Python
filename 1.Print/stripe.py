name = input('Please enter your full name. ')

# remove all empty or whitespace around the message
name = name.strip()
name = name.title()

print(f"Hi, {name}")

print('===============================')

name = name.strip().title()

print(f"Hi, {name}")


print(f"Hi, {name}", end=' << ')

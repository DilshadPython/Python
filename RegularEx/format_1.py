import re

name = input("Enter your name: ").strip()

# re.search()

# search for full name
# if we define the var to a regular exression all in one line we have to use :=
# if matches := re.search(r"^(.+), *(.+)$", name): one way or

if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"Your name is {name}")
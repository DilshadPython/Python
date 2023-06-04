# strip() remove the whitespace and title() capitalize the first letter of firstname and lastname
# Notice strip() remove the white space from beginning and the end of the name not in between
fullname = input('Enter you full name:  ').strip().title()

print(f'Hello, {fullname}')
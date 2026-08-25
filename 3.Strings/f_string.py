'''
How to use f strings
'''

name = str(input('Enter a name: '))
lang = str(input('Enter a language: '))

print(f'Hello {name}, do you like to learn {lang} programming language?, ')

print('#################################################################')

new_name = ''
text = 'Hello, ' + input("Enter a name: ")

print(text + f"{new_name}")

my_name = 'Azad'
print()
print(f"Hello, {my_name.upper()}")

age = 37
txt = f'My name is {my_name} and I am {age} years old'
print(txt)


print("\n Display all methods use with string: \n")
print(dir(my_name))
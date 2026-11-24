print('Show the str:')
x = 'Hello Python'
print(type(x))

print('========')
print('Display int')
num = 56
print(type(num))

print('\n=======')
print('Display float')
number = 33.27
print(type(number))

print('\n=======')
print('Display complex')
y = 2j
x = 10j
print(y)
print(type(y))
print(x)
print(type(x))

print('=======')
print('Display list')
lang = ['Python', 'Java']
print(type(lang))

print('=======')
print('Display tuple')
names = ('Julia', 'Adam', 'George')
print(type(names))

print('\n=======')
print('Display range')
num = range(6)
print(num)
for i in num:
    print(i)
print(type(num))

print('\n=======')
print('Display dictionary')
names = {'fname': 'Julia', 'lastname': 'Adam', 'age': 36}
print(type(names))

print('\n=======')
print('Display set')
names = {'Adam', 'Tom', 'Sammy', 'Tom', 'John', 'Adam'}
print(names)
print(type(names))

print('\n=======')
print('Display frozenset')
fruits = frozenset({"apple", "banana", "cherry","orange"})
print(fruits)
print(type(fruits))

print('\n=======')
a = True
b = False
print(a)
print(b)
print(type(a), type(b))

print('\n=======')
name = b'Python'
print(name)
print(type(name))

print('\n=======')
number = bytearray(7)
print(number)
print(type(number))

print('\n=======')
nums = memoryview(bytes(7))
print(nums)
print(type(nums))

print('\n=======')
x = None
print(x)
print(type(x))

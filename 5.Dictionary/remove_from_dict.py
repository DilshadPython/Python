
post = dict(stid='0814747', fullname='Dilshad Abdulla', university='Anglia Ruskin University',
            location='44.2658974, -102.5586589', language='English')

print('')
print('####################################')
for key in post.keys():
    value = post[key]
    print(key, ' = ', value)


print('')
print('####################################')

new_dict = post.pop(key)
# print(new_dict)

print('')
print('####################################')
for key in post.keys():
    value = post[key]
    print(key, ' = ', value)

print()
print('Removed from the end of the dict look at the loop')
new_dict = post.pop(key)
# print(new_dict)

print('')
for key in post.keys():
    value = post[key]
    print(key, ' = ', value)

print()

new_dict = post.clear()

print('We removed all using clear()')
print()
for key in post.keys():
    value = post[key]
    print(key, ' = ', value)

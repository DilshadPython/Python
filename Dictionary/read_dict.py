
post = dict(stid='0814747', fullname='Dilshad Abdulla', university='Anglia Ruskin University',
            location='44.2658974, -102.5586589', language='English')

print(post)

print('')
print('####################################')
for key in post.keys():
    value = post[key]
    print(key, ' = ', value)

print()
print('####################################')
print()
for key, value in post.items():
    print(key, ' = ', value)

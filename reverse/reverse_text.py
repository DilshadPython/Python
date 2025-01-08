

msg = '''On a Mac keyboard, hitting Shift, Option, and number Two will type out the EUR sign.'''

print(msg)
print('\n')

messages = msg.split()  # split by space
messages.reverse()

msg = ' '.join(messages)
print(msg)

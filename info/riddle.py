myopinion = {
    True: 'yes',
    1: 'no',
    0.1: 'maybe',
    False: 0,
    1.1: 'not sure'
}

print(myopinion)

print()
for key, value in myopinion.items():
    print(key, '', value)

import uuid

for _ in range(10):
    x = uuid.uuid1()
    print(x)

print('')

# for _ in range(6):
#     y = uuid.uuid3()
#     print(y)

print('')

for _ in range(4):
    z = uuid.uuid4()
    print(z)

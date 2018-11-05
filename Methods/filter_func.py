
import statistics


data = [2.3, 12, -0.7, 6.7, 3.13, 22.03, 9.11]

avarage = statistics.mean(data)

print('The avarage: ', avarage)

# now we use filter
print()
print(filter(lambda x: x > avarage, data))

print()
print('Above avarage')
print(list(filter(lambda x: x > avarage, data)))

print()
print('Below avarage')
print(list(filter(lambda x: x < avarage, data)))

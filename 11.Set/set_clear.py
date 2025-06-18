elements = set(['hello', 23, 'A', 2.36, 'Hello world'])

print(elements)

elements.clear()

print('')
print(elements)

odds = set([11, 13, 15, 17, 19, 21, 1, 3, 5, 7, 9])

evens = set([22, 20, 18, 16, 14, 12, 10, 2, 4, 6, 8])

primes = set([2, 3, 5, 7])

composites = set([4, 6, 8, 9, 10])

# use union() methods to joining two sets also update()
resutls = odds.union(evens)

print(resutls)
print('')
print(evens)
print('')
print(odds)

print('')
print(odds.intersection(primes))

print('')
print(primes.intersection(evens))

print('')
evens.intersection(odds)

print('')
primes.union(composites)

dir(primes)

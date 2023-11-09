''' 
	A tuple is a sequence of immutable Python objects. Tuples are sequences,
	just like lists. The only difference is that tuples can't be changed i.e.,
	tuples are immutable and tuples use parentheses and lists use square brackets.
	Creating a tuple is as simple as putting different comma-separated
	values and optionally you can put these comma-separated values between
	parentheses also. For example:
'''

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = ("a", "b", "c", "d")
tup4 = ()

print(tup1)
print(tup2)
print(tup3)
print(tup4)

print('#############')
print(tup1[1])
print(tup2[3])
print(tup3[0])

print('#############')
print(tup3[::-1])
print(tup3[:-1])

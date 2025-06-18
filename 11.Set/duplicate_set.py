fruites = {'apples', 'oranges', 'cherry', 'bananas', 2.7}
num = {21, 9, 2.7, 0.66 -5, 'oranges'}

"""
The update() method inserts all items from one set into another.

The update() changes the original set, and does not return a new set.
"""
print('==== x ====')
x = fruites.union(num)
print(x)

print('===================\n')
## Keep the items that exist in both fruites, and num:
fruites.intersection_update(num)
print(fruites)
print('====================\n')

first = {'Hello', 22, 'Python', 'Java', 7, 9, True}
second = {9, 'Java', 22, True, 'Python', 'JavaScript', False}
last = first.intersection(second)
print(last)

print('====================\n')
# Keep all items from first that are not in second:
y = first.difference(second)
print(y)

print('====================\n')
one = {8, 'Hello', 22, 'Python', 'Java', 7, 9, True}
two = {9, 'Java', 22, True, 'Python', 'JavaScript', False, 6}

three = one - two
print(three)

# You can use the - operator instead of the difference() method, and you will get the same result.
print('====================\n')
four = two - one
print(four)

print('====================\n')
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
a.difference_update(b)
print(a)

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
print('====================\n')
ab = {"apple", "banana", "cherry"}
ac = {"google", "microsoft", "apple"}
dd = ab.symmetric_difference(ac)
print(dd)

# Use ^ to join two sets:
print('====================\n')
cc = ab ^ ac
print(cc)

#Use the symmetric_difference_update() method to keep the items that are not present in both sets:
print('====================\n')
aa = {"apple", "banana", "cherry", "orange"}
bb = {"google", "microsoft", "apple", "yahoo"}
aa.symmetric_difference_update(bb)
print(aa)
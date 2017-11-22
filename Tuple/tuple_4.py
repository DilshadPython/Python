def example(a, b, c):
    return a + b * c

#now we crate a tuple here and passing to the function above
items=(4, 3, 7)
# now we call the func and passing items to the func [ one star * stand for tuple ]
print(example(*items))


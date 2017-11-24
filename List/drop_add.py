def take(num, lyst):
    rlist = []
    for i in range(0, num):
        rlist.append(lyst[i])
    return rlist


def drop(num, lyst):
    rlist = []
    for i in range(num, len(lyst)):
        rlist.append(lyst[i])
    return rlist

names = ['Dilshad', 'Nick', 'Sam', 'David', 'Tim', 'Geoprg', 'Robert']
somenames = take(3, names)
print(somenames)
somenames = take(-3, names)
print(somenames)

names = drop(3, names)
print(names)
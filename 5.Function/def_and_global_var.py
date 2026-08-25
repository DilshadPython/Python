x = 1
y = 2
z = 3


def bar(xx):
    global y
    x = 4
    xx = 5
    y = 6
    z = 7

print(bar(x))

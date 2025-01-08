import timeit


def test_me(mydict, key):
    return mydict[key]


print(timeit.timeit('test_me(mydict, key)',
            setup="from __main__ import test_me; mydict = {'a': 5, 'b': 6, 'c': 7}; key='c'",
            number=10000))

'''
LEGB
Is stand for Local, Enclosing, Global, Built-in
'''

lang = 'global Python3'


def legb():
    # we define the lang as global for test
    global lang
    lang = 'local Python2'
    print(lang)


legb()
print(lang)
#display here local for both because we define the lang global inside the func which is local for both display python2
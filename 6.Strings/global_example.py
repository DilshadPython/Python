def like_func():
    global language
    language ='Python'

print('Not return any message')
like_func()

print('\nDisplay the global word')
print('I love ', language)

print('\nDisplay the global word')
lang = 'JavaScript'

def myfunc():
    global lang
    lang = 'Java'

myfunc()

print('I like this language ' + lang)
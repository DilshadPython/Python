import builtins

for index, func in enumerate(dir(builtins)):
    print(index, func)

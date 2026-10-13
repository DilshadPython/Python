def register_client(name, age, *args):
    print(name, age)
    print('args contains:', args)

register_client('Alice', 25)
register_client('Bob', 28)
register_client('Charlie', 23, 'London')
register_client('David', 31, 'david@live.com')
register_client('Sam', 33, 'Berlin', 'sam@gmail.com')
register_client('Eliot', 24, 'Germany', 'Musican', '07754 2144 2547')

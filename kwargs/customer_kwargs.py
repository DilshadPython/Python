def register_customer(*args, **kwargs):
    print('arg contains', args)
    print('kwargs contains:', kwargs)
    for key, value in kwargs.items():
        print('--->', key, ':', value)

register_customer('Alice', 25)
register_customer('Bob', 28)
register_customer('Charlie', 23, city='London')
register_customer('David', 31, email='david@live.com')
register_customer('Sam', 33, city='Berlin', email='sam@gmail.com', country='Germany')
register_customer('Eliot', 24, 'UK', job='Musican', mobile='07754 2144 2547')


def drinks_type(*names, **details):
    print('List of any kind of Alcohols')
    for name in names:
        print(f' -- {name}')

    for key, value in details.items():
            print(f' -- {key}: -- {value}')

drinks_type("Whisky", 25.99, no_alcohol='Wine', tyep='Jack Daniles')
drinks_type('Gen', 19.90, type='Monkey Shoulders', wine='Red wines')
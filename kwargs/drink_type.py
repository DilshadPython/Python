def drinks_type(name, price, **details):
    print(f'Beer:  {name}')
    print(f'2.99: {price}')

    if details:
        print(details)
        for key, value in details.items():
            print(f' -- {key}: -- {value}')

drinks_type("Whisky", 25.99, no_alcohol='Wine', tyep='Jack Daniles')
drinks_type('Gen', 19.90, type='Monkey Shoulders', wine='Red wines')

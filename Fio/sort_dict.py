
with open("dict_city.csv") as f:
    for name in f:
        # we split the city and county by ,
        row = name.rstrip().split(',')
        #dict[ Key , Value ]
        print(f"{row[0]} is in {row[1]}")
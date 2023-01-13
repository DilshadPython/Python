# This is called count controll loop

balance = 800
rate = 1.05
year = 1

# while the year is less than 20 years
while year <= 20:
    # calculate the balance by the rate
    balance = balance * rate
    # Showing each year and the balance changed
    print('Year : ' + str(year) + ': ' + str(balance))
    # How is change when the year increased 
    year = year + 1

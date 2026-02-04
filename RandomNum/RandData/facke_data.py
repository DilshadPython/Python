import random

fname = ['James', 'Barbara', 'Michael', 'David', 'Patricia', 'Karen',
         'Daniel', 'Richard', 'Lisa', 'Anthony', 'Rebecca']

lname = ['Smith', 'Morris', 'Cooper', 'Watson', 'Williams', 'Ross',
         'Jenkins', 'Perry', 'Bell', 'Gibson', 'Castillo']

str_name = ['Guild Road', 'Harvest Drive', 'Heska Road', 'Ilona Park Road', 'Lane Street', 'McKay Road',
            'Nation', 'Lytton Court', 'Patio Lane', 'Oliva str', 'Shay Drive']
post_codes = ['M1 1AE', 'NW3 1W', 'CR2 6XH', 'DN55 1PT', 'B33 8TH', 'W1A 0AX', 'EC1 4EC', 'CB1 22EH',
              'PO1 1AA', 'EC1A 1BB ', 'S1–S36']

cities = ['Camden', 'Munich', 'Zaragoza', 'Tilburg', 'Vaasa', 'Krakow',
          'Lisbon', 'Fermo', 'Chelmsford', 'London', 'Lion']
states = ['Nebraska', 'Virginia', 'South Dakota', 'Kansas', 'Barking', 'Dagenham',
          'Louisiana', 'Romford', 'Maine', 'Alabama', 'West Ham', 'Cambine']

for num in range(70):
    f_name = random.choice(fname)
    l_name = random.choice(lname)

    mobile =f'\t +44 078 {random.randint(100,999)} {random.randint(10 ,99)}{random.randint(100,999)}'

    house_number = random.randint(10, 99)
    address = random.choice(str_name)
    state = random.choice(states)
    city = random.choice(cities)
    post_code = random.choice(post_codes)

    addr = f'\t {house_number} {address}\n\t {state}\n\t {city}\n\t {post_code}'

    mail = '\n\t ' + f_name.lower() + '.' + l_name.lower() + '@mail.com'

    print(f'\t {f_name} {l_name}\n {addr}\n  {mail}\n {mobile}\n')



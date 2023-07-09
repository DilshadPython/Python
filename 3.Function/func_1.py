print('Enter your gender, m, f or None')

sex = str(input('Enter your gender: '))

def get_gender(sex=None):
    if sex == 'm':
        sex = 'Male'
    elif sex == 'f':
        sex = 'Female'
    elif sex == None:
        sex = 'None'
    else:
        sex = 'Not ins the list'

    print(sex)

get_gender(sex)

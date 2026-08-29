
user_1 = {'id': 3, 'fname': 'Tim', 'lname': 'John', 'email':
          'tim.john@icloud.com', 'linkedin': True}

user_2 = {'id': 5, 'fname': 'Dielman',
          'lname': 'Ary', 'email': 'dielman.ary@icloud.com', 'linkedin': False}

user_3 = {'id': 7, 'fname': 'Holly', 'lname': 'Smith', 'email':
          'holly.smith@icloud.com', 'twetter': True}

user_4 = {'id': 9, 'fname': 'Alan',
          'lname': 'Cory', 'email': 'alan.cory@icloud.com', 'twetter': False}

print('Id', 'Fname', 'Lname', 'Email')
for user_detail in user_1, user_2, user_3, user_4:
    print(user_detail['id'], user_detail['fname'], user_detail['lname'],
          user_detail['email'])


print('##################################################\n')
'''
Here we have two difference social media with True or False
we search for the using if method
'''
print('Id', 'Fname', 'Lname', 'Email', 'SocialMedia')

for detail in user_1, user_2, user_3, user_4:
    if 'linkedin' in detail:
        print(detail['id'], detail['fname'], detail['lname'],
              detail['email'], detail['linkedin'])
    elif 'twetter' in detail:
        print(detail['id'], detail['fname'], detail['lname'],
              detail['email'], detail['twetter'])
    else:
        print('There is no Social media column')

print('*************************************************\n')

'''
Now we select users with twetter and linked in
'''
# create empty dictionary
twetter_user = {}
user_has_twetter = True

linkedin_user = {}
user_has_linkedin = True

print('Select only users has twetter or linkedin account')
for user in user_1, user_2, user_3, user_4:
    if 'twetter' in user:
        if user['twetter'] == user_has_twetter:
            twetter_user = user
        else:
            user
    elif 'linkedin' in user:
        if user['linkedin'] == user_has_linkedin:
            linkedin_user = user
        else:
            user
    else:
        pass

print(twetter_user)
print(linkedin_user)

print('=========================================\n')

print('We search throw is numbers all the user has the id in the list of numbers')

for x in range(0, 10):
    for user in user_1, user_2, user_3, user_4:
        if user['id'] == x:
            print(user)

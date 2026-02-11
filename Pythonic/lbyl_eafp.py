# Duck typing and Easier to ask forgiveness than permission (EAFP)

# person = {
#     "name": "David",
#     "age": 20,
#     "job": "Software Engineer",
#     "email": "david@software.com"
# }

person = {
    "name": "David",
    "age": 20,
    "job": "Driver"
}

# LBYL Non-Pythonic
# if 'name' in person and 'age' in person and 'job' in person:
#     print("\n\t I'm {name}. I'm {age} years old and I am a {job}, my {email} address are correct.".format(**person))
# else:
#     print("\n\t Missing some keys")

# EAFP Pythonic
try:
    print("\n\t I'm {name}. I'm {age} years old and I am a {job}, my {email} address are correct.".format(**person))
except KeyError as e:
    print("\n\t Missing {} keys".format(e))
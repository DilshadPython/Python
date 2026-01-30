cars = ['Audi', 'Mercedes', 'BMW', 'Ford']
models = ['A7', 'A20', 'XM', 'F16']

zipped = list(zip(cars, models))
print(zipped)

empty_dict = {}
for car, model in zip(cars, models):
    empty_dict[car] = model
print(empty_dict)

# use list comprehensions
new_dict = dict(zip(cars, models))
print(new_dict)

a_values = list(new_dict.values())
print(a_values)

b_keys = list(new_dict.keys())
print(b_keys)

# dictionary comprehensions
c_list = {car: model for car, model in zip(cars, models)}
print(c_list)

# we remove one of the cars dictionary comprehension
d_list = {car: model for car, model in zip(cars, models) if car != 'Mercedes'}
print(d_list)

# create set comprehensions
e_set = {x for x in models}
print(e_set)

f_set = {y for y in cars}
print(f_set)

# How to add two sets comprehensions use |
total = e_set | f_set
print(total)

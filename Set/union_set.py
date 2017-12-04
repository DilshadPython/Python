blue_eyes = {'Mandy', 'Thomas', 'Sophy', 'Ebra', 'Ela', 'George'}
blond_hair = {'Klara', 'Hemen', 'George', 'Stuwart', 'Adam', 'Mandy', 'Sophy'}
o_blood = {'Thomas',  'Ebra', 'Ela', 'Adam'}
a_blood = {'Mandy', 'Hemen'}
b_blood = {'Klara', 'George', 'Sophy'}
ab_blood = {'Stuwart'}

print(blue_eyes.union(blond_hair))
print('-------------------------------------------------------')
print(blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes))

print('-------------------------------------------------------')
print(blue_eyes.intersection(blond_hair))
print(blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes))

print('-------------------------------------------------------')
print(blond_hair.difference(blue_eyes))
print(blond_hair.difference(blue_eyes) == blue_eyes.difference(blond_hair))

print('-------------------------------------------------------')
print(blond_hair.symmetric_difference(blue_eyes))
print(blond_hair.symmetric_difference(blue_eyes) == blue_eyes.symmetric_difference(blond_hair))

print('-------------------------------------------------------')
print(o_blood.issubset(blond_hair))
print(o_blood.issubset(blue_eyes))

print('-------------------------------------------------------')
print(a_blood.isdisjoint(o_blood))
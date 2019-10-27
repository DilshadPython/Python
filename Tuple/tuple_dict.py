mydictionary = dict()

mydictionary['Hello'] = 7
mydictionary['Python'] = 9

for k,v in mydictionary.items():
	print(k, v)

# change the dictionary to tuple
tup = mydictionary.items()
print(tup)

# this will check the first
(0, 3, 7) <  (1, 3, 7)
print((0, 3, 7) <  (1, 3, 7))

(0, 3, 17) <  (0, 3, 7)
print((0, 3, 17) <  (0, 3, 7))

# here check only the len of the string 
('Azad', 'Dilsad', 'Shvan') > ('Ali', 'Alphabet', 'Tom')
print(('Azad', 'Dilsad', 'Shvan') > ('Ali', 'Alphabet', 'Tom'))
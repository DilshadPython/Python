import random

miles_has_feet = 5280
km_has_meter = 1000

names = ['Dilshad', 'Azad', 'Tom', 'Claudia']


def get_file_ext(filename):
	return filename(filename.index('.') + 1)


def roll_dice(number):
	return random.randint(1, number)

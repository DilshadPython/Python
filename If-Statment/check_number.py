week = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

print(week)


def main():
    day = str(input('Enter a day from the list above: \n'))
    if is_off(day):
    	print(f'{day} is OFF, WEEKEND')
    else:
   		print(f'{day} is ON working day')


def is_off(d):
	if d not in week or d == int(d):
		return False
	return True if d == week[5] or d == week[6] else False


main()

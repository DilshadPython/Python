def fahrenheit_temp(temp):
	return (temp - 32.0) * (5.0 / 9.0)
 

def celsius_temp(temp):
	return temp * (9.0 / 5.0) + 32.0


# here is we use multiple argument in the function
def convert_temp_to(temp, to_celsi):
	if to_celsi.lower() == 'c':
		return fahrenheit_temp(temp)
	else:
		return celsius_temp(temp)

temp=int(input('Enter a temperature of today: '))

# Here you have to enter c if you want celsius or f if you want fahrenheit
celsi=str(input('Enter the celsius to convert to: '))

converted_temp = convert_temp_to(temp, celsi)

print(temp, converted_temp, celsi)
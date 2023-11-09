# local varable can get access only in the place where created 
# example create var inside the function we can get access outside function

def cal_sum(number):
	# result is local varable created inside the func
	result = number + number
	return result

print(cal_sum(9))

# now we try to get access to result outside func
# print(result) << this way the program will crashed
print('Access to result outside the function.')
try:
	print(result)
except Exception as e:
	print('***' * 20)
	print("\nCan't get access to local varable created inside the function!")

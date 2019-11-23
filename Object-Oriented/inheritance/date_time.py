'''
Date and Time
'''
class Date(object):
	def get_date(self):
		return '2019-11-21'


class Time(Date):
	"""docstring for Time"""
	def get_time(self):
		return '12:01 PM'

date_obj = Date()
print(date_obj.get_date())
''' The object of parent class can not call the method in subclass 
	print(date_obj.get_time())
	Traceback (most recent call last):
  	File "university.py", line 16, in <module>
    print(date_obj.get_time())
	AttributeError: 'Date' object has no attribute 'get_time'
'''

time_obj = Time()
print(time_obj.get_time())
''' The object in child class can access and call the method in parent class '''
print(time_obj.get_date())
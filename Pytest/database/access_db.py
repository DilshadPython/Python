# create university database
class University:
	# initialse the class
	def __init__(self):
		self.connection = Connection()

	def access(self, access_start):
		return self.connection


class Connection:

	def __init__(self):
		self.cur = Cursor()

	def cursor(self):
		return self.cur 

	def close(self):
		pass


class Cursor():

	def execute(self, query):
		if query == 'select id from university_db where name=Dilshad':
			return 814747
		elif query == 'select id from university_db where name=Rachel':
			return 804878
		else:
			return -1

	def close():
		pass



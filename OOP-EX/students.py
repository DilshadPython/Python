class Student:
	# attributes of fields name, id, grades(list)
	grades = []
	def __init__(self, name, id):
		self.name = name
		self.id = id

	# we create another arg here as var to use for adding num to grades
	def add_grade(self, grade):
		# we adding grade to grades list
		self.grades.append(grade)


	def display_grade(self):
		addgrd = ''
		# important has call grades list throw self.grades
		for grade in self.grades:
			addgrd += str(grade) + ' '
		return addgrd

# define object std
std = Student('Joe', '1234')

# we are adding the grade to the list
std.add_grade(77)
std.add_grade(63)
std.add_grade(90)
std.add_grade(69)

# now we try to reterive the dages of this student
print(std.name, std.id)
print(std.display_grade())


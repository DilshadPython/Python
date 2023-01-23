class School:
	def staff(self):
		print('\nTeachers and students are both going to schools in the running time.')
		print('\nSelf is the first arg call in the methods automaticall sometimes called bound methods.')
		print('\n This self instance object display address in memory internal to the methods of the class.')
		print(self)

	def department(self, primary):
		self.primary = primary
		return str(self.primary) + ' schools are starting from class 1 -5' 

print('\nThis the class name')
print(School)
obj_stf = School()

obj_stf.staff()
print('\n This is obj_stf instance object to the School outside the Class display same address in memory of self of methods.')
print(obj_stf)

print(obj_stf.department('Primary'))
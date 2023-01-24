class MaxSizeList:

	names = []

	def __init__(self, number):
		self.number = number

	def push(self, name):
		self.names.append(name)
		return self.names

	def get_list(self):
		list_name = ''
		for name in self.names:
			list_name += str(name) + ' '
		return list_name


# myobj = MaxSizeList()

# myobj.push('Python')
# myobj.push('Javas')
# myobj.push('C++')
# myobj.push('JavaScript')

# print(myobj.get_list())
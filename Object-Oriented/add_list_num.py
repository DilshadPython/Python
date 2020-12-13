class ListNumber(object):
	def __init__(self, new_num):
		self.main_list = new_num

	def __add__(self, second_num):
		mylst = [x + y for x, y in zip(self.main_list, second_num.main_list)]

		return ListNumber(mylst)

	def __repr__(self):
		return str(self.main_list)


flst_1 = ListNumber([1, 2, 3, 4, 5, 6, 3, 4])
slst_2 = ListNumber([10, 100, 200, 3000, 500, 400, 800, 700])

total = flst_1 + slst_2
print(total)


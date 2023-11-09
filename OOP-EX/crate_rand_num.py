# we are importing the random from python lib
import random 

class Number:
	def display_rand(self):
		self.rand_num = random.randint(1, 20)
		# we don't need to return because automaticall return self.rand_num
		# return self.rand_num


obj = Number()
obj.display_rand()

print(obj.rand_num)
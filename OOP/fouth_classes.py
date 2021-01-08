class Point:

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		self.coords = (self.x, self.y)


	def move(self, x, y):
		self.x += x
		self.y += y

	# In this case p1 become self and p2 become p.y
	def __add__(self, p):
		return Point(self.x + p.x, self.y + p.y)

	def __sub__(self, p):
		return Point(self.x - p.x, self.y - p.y)

	def __mul__(self, p):
		return self.x * p.x + self.y * p.y


	def __len__(self):
		import math
		return math.sqrt(self.x ** 2 + self.y ** 2)

	def __gt__(self, p):
		return self.length() > p.length()

	def __ge__(self, p):
		return self.length() >= p.length()

	def __lt__(self, p):
		return self.length() < p.length() 

	def __le__(self, p):
		return self.length() <= p.length()

	def __eq__(self, p):
		return self.length() == p.length() and self.y == p.y

	def __str__(self):
		return "(" + str(self.x) + ', ' + str(self.y) + ")"

p1 = Point(4, 5)
p2 = Point(7, 9)
p3 = Point(1, 4)
p4 = Point(7, 3)

len(p1)
p5 = p1 + p3
p6 = p2 - p4
p7 = p3 * p4

print(p5, p6, p7)

# Base class
class Shape:
	def __init__(self, xcor, ycor):
		self.x = xcor
		self.y = ycor


	def __str__(self):
		return ' x: ' + str(self.x) + ', y: ' + str(self.y)


	def move(self, x1, y1):
		self.x = self.x + x1
		self.y = self.y + y1

# this is a drive class inheriate from base class
class Rectangle(Shape):
	def __init__(self, xcor, ycor, height, width):
		Shape.__init__(self, xcor, ycor)
		self.height = height
		self.width = width


	def __str__(self):
		# we bring the shape of Shape class below as a new line assigned to the_shape
		the_shape = Shape.__str__(self) + ', height: ' + str(self.height) + \
					', width: ' + str(self.width)
		return the_shape

# rec = Rectangle(xcor, ycor, height, width)
rec = Rectangle(6, 18, 9, 12)
print(rec)
print()
rec.move(7, 11)
print(rec)
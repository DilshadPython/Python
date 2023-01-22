class Point:
	def __init__(self, x, y):
		self.point = (x, y)


	def __str__(self):
		return 'x: ' + str(self.point[0]) + ', y: ' + str(self.point[1])
    
	def getLocation(self, x, y):
		self.point = (x, y)


class Line:
	def __init__(self, p1, p2):
		self.point1 = p1
		self.point2 = p2

	def __str__(self):
		return 'Point 1: ' + str(self.point1) + '\n' +'Point 2: ' + str(self.point2)

point1 = Point(1, 2)
print(point1)
point1.getLocation(5, 7)
print(point1)

point2 = Point(5, 6)
line1 = Line(point1, point2)
print(line1)
point2.getLocation(88, 33)
print(point2)
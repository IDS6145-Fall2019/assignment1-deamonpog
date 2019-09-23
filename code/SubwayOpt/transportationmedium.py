class transportationMedium:
	def __init__(self, p1, p2, d, a):
		self.end1 = p1
		self.end2 = p2
		self.length = d
		self.area = a
		self.isTwoWay = False
		self.capacity = 2
		self.directionEnd1ToEnd2 = True
		self.people = []
	
	def Transport(self, p):
		raise NotImplementedError("Please Implement this method!")
		report False

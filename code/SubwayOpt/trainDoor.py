from door import door

class trainDoor(door):
	def __init__(self,n,a):
		self.name = n
		self.area = a

	def Density(self):
		print("calculating congestion at the door")
		return 0
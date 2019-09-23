from transportationmedium import transportationmedium

class escalator(transportationmedium):

	def __init__(self):
		self.isRotating = True
		self.rotationMoveSpeed = 2
		self.lanes = [ lane(self), lane(self) ]
	
	def Transport(self, p):
		return True

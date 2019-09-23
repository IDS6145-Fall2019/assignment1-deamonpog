from transportationmedium import transportationmedium

class elevator(transportationmedium):

	def __init__(self):
		self.area = 6
		self.moveSpeed = 2
	
	def Transport(self, p):
		return True

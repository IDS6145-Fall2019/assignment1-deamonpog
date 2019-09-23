class train:

	def __init__(self, n, a):
		self.name = n
		self.timeOfArrival = a
		self.timeOfDeley = 2
		self.people = []
	
	def Arrive(self):
		print("Train {} has arrived.".format(self.name))

	def Leave(self):
		print("Train {} has left.".format(self.name))

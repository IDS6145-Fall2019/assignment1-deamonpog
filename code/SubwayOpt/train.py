class train:

	def __init__(self, n, a):
		self.name = n
		self.timeOfArrival = a
		self.timeOfDeley = 2 # time spent in station for people to get on
		self.people = []
	
	def Arrive(self):
		print("Train {} has arrived.".format(self.name))

	def Leave(self):
		print("Train {} has left.".format(self.name))

class pathnode:

	def __init__(self, x, y, z):
		self.position = [x,y,z]
		self.adjecents = []
		print("pos: {},{},{}".format(str(self.position[0]),str(self.position[1]),str(self.position[2])))
	
	def Distance(self, pos):
		return math.sqrt((self.position[0] - pos[0]) ** 2 + (self.position[1] - pos[1]) ** 2 + (self.position[2] - pos[2]) ** 2)

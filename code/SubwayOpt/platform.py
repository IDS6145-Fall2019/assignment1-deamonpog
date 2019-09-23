class platform:

	def __init__(self,n,a):
		self.name = n
		self.area = a
		self.pathnodes = []
	
	def Density(self):
		td = 0
		for pn in self.pathnodes:
			td += pn.Density()
		return td

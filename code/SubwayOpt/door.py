from pathnode import pathnode

class door(pathnode):
	def __init__(self,c):
		self.isOpen = False
		self.perTickCapacity = c

	def Open(self):
		self.isOpen = True

	def Close(self):
		self.isOpen = False
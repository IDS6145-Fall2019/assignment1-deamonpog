
class goal:
	def __init__(self, c, t):
		self.isToCity = c
		self.toTrain = t

	def TimeLeft(self):
		print("calculating time left for the train to arrive if goal is notToCity!")
		return 0
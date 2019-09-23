class person:

	def __init__(self,g,l=False):
		self.isLate = l
		self.goal = g
		self.current = None
		self.position = [0,0,0]
		self.speed = 3
		self.stateAction = ''
		self.behavior = None
		self.ticksSpent = 0
		print("I am alive!")

	def PlanNextAction(self):
		print("Planning action...")

	def Walk(self,target):
		print("Walking towards the" + str(target))

	def ExitTM(self,targetTM):
		print("Exiting the " + str(targetTM))

	def EnterTM(self,targetTM):
		print("Entering the " + str(targetTM))

	def WaitLong(self,wa):
		print("I am waiting..... in the area " + str(wa))

	def WaitShort(self,p):
		print("Waiting for the train on platform " + str(p))

	def Exit(self,):
		print("I'm dead! :(")

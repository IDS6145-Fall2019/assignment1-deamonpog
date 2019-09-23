from behavior import behavior

class comfortBehavior(behavior):
	def __init__(self, t):
		self.congestionThreshold = t

	def PlanNextAction(self):
		print("Evaluating current state and goal to decide next action...")
		return ''
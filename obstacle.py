class Obstacle:
	"""Obstacle object, decreases in size as game goes on, more appear in the game as time goes on"""
	def __init__(self, x_val = 0, y_val):#Y value is at top of screen
		self.x = x_val
		self.x = y_val

	#def getX():			##maybe later
	#	return self.x

	def getY():
		return self.y

	def lower(self, dy = 1):#Possibly change speed too
		self.y = self.getY() - dy

			#Must set up way to delete them when off screen


	def __str__(self):
		
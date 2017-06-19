import pygame

class SpaceShip:  #(pygame.sprite.Sprite)
	def __init__(self, x_val = 0, y_val):
		pygame.sprite.Sprite.init__(self)
		self.image, self.reflect = load_image(img_file, -1)
		self.x = x_val
		self.y = y_val	#Speed?
		self.alive = True

	def collide():
		#Health TBD, possibly able to change size of ship to add or lower difficulty
		self.alive = False

	def getX():
		return self.x

	def getY():
		return self.y

	def move(dx,dy) #Maybe include event, Y axis is Reversed

		#if direction == pygame.K_UP/DOWN/LEFT/RIGHT
		self.x = self.getX() + dx
		self.y = self.getX() + dy

	def update(self):
		print('updating position')

	def __str__(self):
		return str(self.alive)

def test():
	'''Testing Hero Model'''

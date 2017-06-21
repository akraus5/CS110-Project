import pygame
import utility

class Resup:
	"""endpoint object, when collision detected with spaceShip, level completes"""

	def __init__(self, x_val, y_val):#		possibly scrW ,scrH,  sz = 20
		'''
			Initialize resupply model
			args: 	x_val: int, starting x position
					y_val: int, starting y position
			return: None
		'''
		pygame.sprite.Sprite.__init__(self)		#Possibly change picture file depending on size, or set input to controller
		self.image, self.rect = utility.LoadImage('moon.png', -1)
		#self.scrW = scrW
		#self.scrH = scrH
		self.x = x_val #- self.sz // 2
		self.y = y_val #- self.sz // 2

	def getX(self):
		'''
			Get x value of resupply model
			args: None
			return: self.x (int)
		'''
		return self.x

	def getY(self):
		'''
			Get y value of resupply model
			args: None
			return: self.y (int)
		'''
		return self.y

	#def getSz(self):
	#	return self.sz

	def update(self):
		'''
			TBD
			args: None
			return: None
		'''
		print('Updating Position')

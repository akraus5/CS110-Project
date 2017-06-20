import pygame
impor load_image
class Resup:
	"""endpoint object, when collision detected with spaceShip, level completes"""
	def __init__(self, x_val, y_val):#		possibly scrW ,scrH,  sz = 20
		pygame.sprite.Sprite.init__(self)		#Possibly change picture file depending on size, or set input to controller
		#self.image, self.rect = load_image.load_image('.png', -1)
		#self.scrW = scrW
		#self.scrH = scrH
		#self.sz = sz
		self.x = x_val #- self.sz // 2
		self.y = y_val #- self.sz // 2
		
	def getX(self):
		return self.x

	def getY(self):
		return self.y

	#def getSz(self):
	#	return self.sz

	def update(self):
		print('Updating Position')

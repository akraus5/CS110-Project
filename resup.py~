import pygame
import utility

class Resup(pygame.sprite.Sprite):
	"""endpoint object, when collision detected with spaceShip, level completes"""

	def __init__(self, x_val, y_val, restype = 'moon', moving = False):#		possibly scrW ,scrH,  sz = 20
		'''
			Initialize resupply model
			args: 	x_val: int, starting x position
					y_val: int, starting y position
			return: None
		'''
		pygame.sprite.Sprite.__init__(self)		#Possibly change picture file depending on size, or set input to controller
		self.image, self.rect = utility.LoadImage('resup_' + restype + '.png', -1)
		self.rect.center = (x_val,y_val)
		self.moving = moving
		self.i = 1

'''
	def change_dir(self):
		'''
			#Used to automatically change direction after move() is called
			#args: None
			#return: None
		'''
		if (self.rect.x <= 0):
			self.dir = 'right'
		elif (self.rect.right >= WIDTH):
			self.dir = 'left'

'''
	def update(self):
	'''
		if moving:
			i += 1
			if i == 10:
				if (self.dir == 'left'):
					self.rect.x -= self.spd
				if (self.dir == 'right'):
					self.rect.x += self.spd
				i = 1
	'''
	#def getX(self):
		'''
			Get x value of resupply model
			args: None
			return: self.rect.x (int)
		'''
		return self.rect.x

	#def getY(self):
		'''
			Get y value of resupply model
			args: None
			return: self.rect.y (int)
		'''
		return self.rect.y

	#def getSz(self):
	#	return self.sz

	#def update(self):
		'''
			TBD
			args: None
			return: None
		'''
		print('Updating Position')

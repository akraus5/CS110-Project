import pygame
import utility

class Obstacle(pygame.sprite.Sprite):
	"""Obstacle object, decreases in size as game goes on, more appear in the game as time goes on"""

	def __init__(self, x_val, y_val, scrW ,scrH, stDir='right', speed = 1, size = 'small' ):#Y value is at top of screen
		'''
			Initialize Obstacle
			args: 	x_val: int, starting x position
					y_val: int, starting y position
					scrW: int, screen width
					scrH: int, screen height
					stDir: string, starting direction (accepts 'left', 'right', 'up', 'down')
					speed: int, x and y increment amount
			return: None
		'''

		pygame.sprite.Sprite.__init__(self)		#Possibly change picture file depending on size, or set input to controller
		self.image, self.rect = utility.LoadImage('asteroid_' + size + '.png', -1)
		self.scrW = scrW
		self.scrH = scrH
		self.width = self.rect.width
		self.height = self.rect.height
		self.rect.x = x_val - self.width // 2
		self.rect.y = y_val - self.height // 2
		self.dir = stDir
		self.spd = speed

	def getX(self):
		'''
			Get x value of obstacle
			args: None
			return: self.rect.x (int)
		'''
		return self.rect.x

	def getY(self):
		'''
			Get y value of obstacle
			args: None
			return: self.rect.y (int)
		'''
		return self.rect.y

	#def getSz(self):
		#return self.sz

	def change_dir(self):
		'''
			Used to automatically change direction after move() is called
			args: None
			return: None
		'''
		if (self.rect.x <= 0):
			self.dir = 'right'
		elif (self.rect.x + self.width >= self.scrW):
			self.dir = 'left'
		if (self.rect.y <= 0):
			self.dir = 'down'
		elif (self.rect.y + self.height >= self.scrH):
			self.dir = 'up'###mess with speed maybe

	def move(self):
		'''
			Used to move automatically
			args: None
			return: None
		'''
		if (self.dir == 'left'):
			self.rect.x -= self.spd
		if (self.dir == 'right'):
			self.rect.x += self.spd
		if (self.dir == 'up'):
			self.rect.y -= self.spd
		if (self.dir == 'down'):
			self.rect.y += self.spd

	def update(self):
		'''
			TBD
			args: None
			return: None
		'''
		print('Updating Position')

	#def __str__(self):

import pygame
import utility

class Obstacle:
	"""Obstacle object, decreases in size as game goes on, more appear in the game as time goes on"""

	def __init__(self, x_val, y_val, scrW ,scrH, stDir='right', speed = 1):#Y value is at top of screen
		pygame.sprite.Sprite.__init__(self)		#Possibly change picture file depending on size, or set input to controller
		self.image, self.rect = utility.LoadImage('asteroid.png', -1)
		self.scrW = scrW
		self.scrH = scrH
		self.width = self.rect.width
		self.height = self.rect.height
		self.x = x_val - self.width // 2
		self.y = y_val - self.height // 2
		self.dir = stDir
		self.spd = speed

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	#def getSz(self):
		#return self.sz

	def change_dir(self):
		if (self.x <= 0):
			self.dir = 'right'
		elif (self.x + self.width >= self.scrW):
			self.dir = 'left'
		if (self.y <= 0):
			self.dir = 'down'
		elif (self.y + self.height >= self.scrH):
			self.dir = 'up'###mess with speed maybe

	def move(self):
		if (self.dir == 'left'):
			self.x -= self.spd
		if (self.dir == 'right'):
			self.x += self.spd
		if (self.dir == 'up'):
			self.y -= self.spd
		if (self.dir == 'down'):
			self.y += self.spd
	def update(self):
		print('Updating Position')

	#def __str__(self):

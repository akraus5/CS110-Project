import pygame
import utility

class Obstacle(pygame.sprite.Sprite):
	"""Obstacle object, decreases in size as game goes on, more appear in the game as time goes on"""

	def __init__(self, x_val, y_val, scrwidth,scrheight, stDirx=None,stDiry=None, speed = 3, size = 'small'):
		'''
			Initialize Obstacle
			args: 	x_val: int, starting x position
					y_val: int, starting y position
					scrW: int, screen width
					scrH: int, screen height
					stDirx: string, starting direction (accepts 'left', 'right')
					stDirx: string, starting direction (accepts 'up', 'down')
					speed: int, x and y increment amount
			return: None
		'''

		pygame.sprite.Sprite.__init__(self)

		self.image, self.rect = utility.LoadImage('asteroid_' + size + '.png', -1)
		self.rect.center = (x_val,y_val)
		self.dirx = stDirx
		self.diry = stDiry
		self.spd = speed
		self.scrwidth = scrwidth
		self.scrheight = scrheight

	def setX(self,x):
		self.rect.x = x

	def setY(self,y):
		self.rect.y = y

	def change_dir(self, collide = False):
		'''
			Used to automatically change direction after move() is called
			args: None
			return: None
		'''

		if collide:
			if self.dirx == 'right':
				self.dirx = 'left'
			elif self.dirx == 'left':
				self.dirx = 'right'
			else:
				self.dirx = 'left'
			if self.diry == 'up':
				self.diry = 'down'
			elif self.diry == 'down':
				self.diry = 'up'
			else:
				self.diry = 'down'


		if (self.rect.x <= 0):
			self.dirx = 'right'
		elif (self.rect.right >= self.scrwidth):
			self.dirx = 'left'
		if (self.rect.y <= 0):
			self.diry = 'down'
		elif (self.rect.bottom >= self.scrheight):
			self.diry = 'up'

	def update(self):
		'''
			Used to move automatically
			args: None
			return: None
		'''
		
		if (self.dirx == 'left'):
			self.rect.x -= self.spd
		elif (self.dirx == 'right'):
			self.rect.x += self.spd
		if (self.diry == 'up'):
			self.rect.y -= self.spd
		elif (self.diry == 'down'):
			self.rect.y += self.spd

		self.change_dir()


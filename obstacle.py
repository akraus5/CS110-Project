import pygame
import utility

class Obstacle(pygame.sprite.Sprite):
	"""Obstacle object, decreases in size as game goes on, more appear in the game as time goes on"""

	def __init__(self, x_val, y_val, scrwidth,scrheight, stDirx=None,stDiry=None, speed = 3, size = 'small'):
		'''
			Initialize Obstacle
			args: 	x_val:	int, starting x position
					y_val:	int, starting y position
					scrwidth/scrheight: int, hwight and width of screen, used to keep obj in bounds
					stDiryirx: string, starting direction (accepts 'left', 'right')
					stdDiry: string, starting direction (accepts 'up', 'down')
					speed: int, speed of movement
					size: string, size of obstacle (accepts  'small','medium','large')
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

	def setX(self,x):
		'''
			change rect.x value using x parameter
			args: x (int, new x value)
			return: None
		'''
		self.rect.x = x

	def setY(self,y):
		'''
			change rect.y value using y parameter
			args: y (int, new y value)
			return: None
		'''
		self.rect.y = y

	def change_dir(self, collide = False):
		'''
			Used to automatically change direction before (when checking collisions) and after update() is called
			args: collide: bool, if collide triggered True, then determines how collision idrection should be changed.
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
			Used to move automatically, calls change_dir at end to check bounds
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

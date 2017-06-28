import pygame
import utility

class Resup(pygame.sprite.Sprite):
	"""endpoint object, when collision detected with spaceShip, level completes"""

	def __init__(self, x_val, y_val, scrwidth,scrheight, restype = 'moon', moving = False, direction = 'right', spd = 1):
		'''
			Initialize resupply model
			args: 	x_val: int, starting x position
					y_val: int, starting y position
			return: None
		'''
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = utility.LoadImage('resup_' + restype + '.png', -1)
		self.rect.center = (x_val,y_val)
		self.scrwidth = scrwidth
		self.scrheight = scrheight
		self.moving = moving
		self.spd = spd
		self.dir = direction

	
	def getX(self):
		'''
			Get x value of resupply model
			args: None
			return: self.rect.x (int)
		'''
		return self.rect.x

	def getY(self):
		'''
			Get y value of resupply model
			args: None
			return: self.rect.y (int)
		'''
		return self.rect.y

	def change_dir(self, collide = False, obdirx = None):
		'''
			Used to automatically change direction before (when checking collisions) and after update() is called, if obstacle and resup move in different directions, resup changes directions
			args: 		collide: bool, checks if any collision occures
					obdirx: string/None: checks if obstacles direction is oppsite of resup, if so, resup changes direction
			return: None
		'''

		if (collide and (obdirx != None) and (self.dir != obdirx)):
			self.dir = obdirx

		if (self.rect.x <= 0):
			self.dir = 'right'
		elif (self.rect.right >= self.scrwidth):
			self.dir = 'left'


	def update(self):
		'''
			Used to move automatically, calls change_dir at end to check bounds
			args: None
			return: None
		'''
		if self.moving:
			if (self.dir == 'left'):
				self.rect.x -= self.spd
			elif (self.dir == 'right'):
				self.rect.x += self.spd
			self.change_dir()



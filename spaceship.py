import pygame
import utility

class SpaceShip(pygame.sprite.Sprite):
	def __init__(self,scrwidth,scrheight,choice = True, spd_x = 5):
		'''
			Initialize SpaceShip
			args: 		image: obj, image sprite of object
					rect: obj, rectangle, set by image
					speed_x: int, changes location of x coordinates on screen
					speed_y: float, increases based on how long up/down keys pressed
					scrwidth/scrheight: int, hwight and width of screen, used to keep obj in bounds
					lucid: bool, used for multiple choice. if True, ship works as expected, if False, left and right keys reversed
			return: None
		'''
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = utility.LoadImage('spaceship.png', -1)
		self.speed_x = spd_x
		self.speed_y = 0
		self.rect.center = (scrwidth//2,scrheight*6/7)
		self.scrwidth = scrwidth
		self.scrheight = scrheight
		self.lucid =choice

	def change_lucid(self,choice):
		'''
			change lucid bool
		'''
		self.lucid = choice

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

	def update(self):
		'''
			Used to move spaceship (change x and y position)
			for x, speed_x is initialized in __init__ and always constant, for speed_y, it is initialized as 0, then increased/decreased based on up/down keys.
			args: 	evnt: event.key, input key
			return: None
		'''
		keys = pygame.key.get_pressed()
		if (keys[pygame.K_UP]):
			self.speed_y += .5

		elif (keys[pygame.K_DOWN]):
			self.speed_y -= .5
		
		self.rect.y -= self.speed_y

		if not (((self.rect.bottom) < self.scrheight)):
			self.rect.y = self.rect.top
			self.speed_y = -1*(self.speed_y) #or -1.5 as a penalty for missing resup
		elif not (self.rect.y > 0): 
			self.rect.y = 0
			self.speed_y = -1*(self.speed_y) #or -1.5 as a penalty for missing resup



		if self.lucid:
			if ((keys[pygame.K_LEFT]) and (self.rect.x > 0)):
				self.rect.x -= self.speed_x

			elif ((keys[pygame.K_RIGHT]) and ((self.rect.right) < self.scrwidth)):
				self.rect.x += self.speed_x
		else:
			if ((keys[pygame.K_LEFT]) and ((self.rect.right) < self.scrwidth)):
				self.rect.x += self.speed_x

			elif ((keys[pygame.K_RIGHT]) and (self.rect.x > 0)):
				self.rect.x -= self.speed_x


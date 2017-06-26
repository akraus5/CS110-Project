import pygame
import utility

class SpaceShip(pygame.sprite.Sprite):
	def __init__(self,scrwidth,scrheight,choice = True, spd_x = 5):
		'''
			Initialize SpaceShip
			args: 	scrwid: int, screen width
					scrht: int, screen height
					speed: int, x and y increment amount
			return: None
		'''
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = utility.LoadImage('spaceship.png', -1)
		self.speed_x = spd_x
		self.speed_y = 0
		self.rect.center = (scrwidth//2,scrheight*6/7)
		self.scrwidth = scrwidth
		self.scrheight = scrheight
		#self.alive = True
		#self.win = False
		#self.sprite
		self.lucid =choice


	#def die(self):
		#Meant to end main loop and end game
		#self.alive = False

	#def winLev(self):
		#Ends subloop for each level
		#self.win = True

	def change_lucid(self,choice):
		self.lucid = choice

	#def getStatus(self):
		#return self.alive,self.win

	#def strtLev(self):#
		##########resets ship parameters for next level
		#self.win = False

	#def getX(self):	#get X val
		'''
			Get x value of spaceship
			args: None
			return: self.rect.x (int)
		'''
		#return self.rect.x

	#def getY(self):	#get Y val
		'''
			Get y value of spaceship
			args: None
			return: self.rect.x (int)
		'''
		#return self.rect.y

	def update(self):
		'''
			Used to move spaceship (change x and y position)
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


		########right, left key:########

			#self.lucid bool, used for multiple choice. if True, ship works as expected, if False, left and right keys reversed
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

	#def __str__(self):
		'''
			Return string status of spaceship
			args: None
			return: self.alive (str)
		'''
	#	return str(self.alive)

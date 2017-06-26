import pygame
import utility

class SpaceShip(pygame.sprite.Sprite):
	def __init__(self, spd_x = 1):
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
		self.rect.center = (WIDTH/2,HEIGHT*6/7)
		#self.alive = True
		#self.win = False
		#self.sprite


	#def die(self):
		#Meant to end main loop and end game
		self.alive = False

	#def winLev(self):
		#Ends subloop for each level
		self.win = True

	#def getStatus(self):
		return self.alive,self.win

	#def strtLev(self):#
		##########resets ship parameters for next level
		#self.win = False

	#def getX(self):	#get X val
		'''
			Get x value of spaceship
			args: None
			return: self.rect.x (int)
		'''
		return self.rect.x

	#def getY(self):	#get Y val
		'''
			Get y value of spaceship
			args: None
			return: self.rect.x (int)
		'''
		return self.rect.y

	def update(self):
		'''
			Used to move spaceship (change x and y position)
			args: 	evnt: event.key, input key
			return: None
		'''
		'''
			possible change, adding acceleration to up and down key, up key accelerates, downkey decellerates.

		########speed becomes speed_x in __init__(), new parameter speed_y.		speed_y starts as zero########
		'''
		keys - pygame.key.get_pressed()
		if (keys[pygame.K_UP]):
			self.speed_y += .5

		elif (keys[pygame.K_DOWN]):
			self.speed_y -= .5
		
		self.rect.y -= self.speed_y

		if not (((self.rect.y + self.shipH) < self.scrht)):
			self.rect.y = self.scrht - self.shipH
			self.speed_y = -1*(self.speed_y) #or -1.5 as a penalty for missing resup
		elif not (self.rect.y > 0): 
			self.rect.y = 0
			self.speed_y = -1*(self.speed_y) #or -1.5 as a penalty for missing resup


		########right, left key:########
		if ((keys[pygame.K_LEFT]) and (self.rect.x > 0)):
			self.rect.x -= self.speed_x

		elif ((keys[pygame.K_RIGHT]) and ((self.rect.right) < WIDTH)):
			self.rect.x += self.speed_x

	#def update(self):
		'''
			TBD
			args: None
			return: None
		'''
		print('updating position')

	#def __str__(self):
		'''
			Return string status of spaceship
			args: None
			return: self.alive (str)
		'''
		return str(self.alive)

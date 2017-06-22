import pygame
import utility

class SpaceShip(pygame.sprite.Sprite):
	def __init__(self, scrwid, scrht, spd = 1):
		'''
			Initialize SpaceShip
			args: 	scrwid: int, screen width
					scrht: int, screen height
					speed: int, x and y increment amount
			return: None
		'''
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = utility.LoadImage('spaceship.png', -1)
		self.scrwid = scrwid
		self.scrht = scrht
		self.speed = spd
		self.shipW = self.rect.width
		self.shipH = self.rect.height
		self.rect.x = (self.scrwid // 2) - (self.shipW // 2)
		self.rect.y = ((self.scrht * 6) // 7) - (self.shipH // 2)	#Speed?
		self.alive = True
		self.win = False
		#self.sprite


	def die(self):
		#Meant to end main loop and end game
		self.alive = False

	def winLev(self):
		#Ends subloop for each level
		self.win = True

	def getStatus(self):
		return self.alive,self.win

	#def strtLev(self):#
		##########resets ship parameters for next level
		#self.win = False

	def getX(self):	#get X val
		'''
			Get x value of spaceship
			args: None
			return: self.rect.x (int)
		'''
		return self.rect.x

	def getY(self):	#get Y val
		'''
			Get y value of spaceship
			args: None
			return: self.rect.x (int)
		'''
		return self.rect.y

	def move(self, evnt):
		'''
			Used to move spaceship (change x and y position)
			args: 	evnt: event.key, input key
			return: None
		'''
		if ((evnt == pygame.K_UP) and (self.rect.y > 0)):
			self.rect.y -= self.speed

		elif ((evnt == pygame.K_DOWN) and ((self.rect.y + self.shipH) < self.scrht) ):
			self.rect.y += self.speed

		if ((evnt == pygame.K_LEFT) and (self.rect.x > 0)):
			self.rect.x -= self.speed

		elif ((evnt == pygame.K_RIGHT) and ((self.rect.x+self.shipW) < self.scrwid)):
			self.rect.x += self.speed

	def update(self):
		'''
			TBD
			args: None
			return: None
		'''
		print('updating position')

	def __str__(self):
		'''
			Return string status of spaceship
			args: None
			return: self.alive (str)
		'''
		return str(self.alive)

#def test():
#	'''Testing Hero Model'''

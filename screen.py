import pygame

class Screen:
	'''Screen object, used for main menue and the game screen, may or may not be seperated into two seperate objects. '''
	def __init__(self, x_cen, y_cen, displaying, color):
		self.screen = pygame.display.set_mode(800,600)
		pygame.display.color(0,0,0)	#Can us picture of space

		#

	def menuScreen(self):	#Main menue screen, set up GUI for menu
		#pygame.set_caption('NAME')

	def frameChange():
		pygame.display.update()

	def endgame(self, SpaceShip):
		if (SpaceShip.alive()):
			#Win game
			#pygame.set_caption('Win')

		else:
			#Game over, close screen
			#pygame.set_caption('Lose')


			pygame.quit()

	def __str__(self, SpaceShip):

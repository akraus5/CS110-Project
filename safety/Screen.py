import pygame

class Screen:
	def __init__(self, x_cen, y_cen, displaying, color):
		pygame.display.init ( )
		pygame.display.color(0,0,0)

		#

	def endgame(self, SpaceShip):
		if (SpaceShip.alive):
			#Win game
		else:
			#Game over, close screen

	def __str__(self, SpaceShip):

'''Event Driven Programming
GUI: Graphical User Interface
Widget, a static box in the window, if clicked, enters event, triggers action
Events -behavior/action, -state
MVC model/view/controller (Design Pattern)
Event driven programming: 
widgets(-state, -behavior), widgets are the Model(NEED TO KNOW!) 
events(-communication, -captures events), events are the Controller 
display(-GUI), display is the View
lab7 will be on model
	\/<---->>Controller<<----->\/
	View			Model'''

import time
import pygame
import Obstacle
import SpaceShip
import screen

class Controller:
	"""Main clas of game, all actions occure in this class"""

	def __init__(self)
		pygame.init()
		self.screen = screen.Screen()	#later
		self.background = pygame.Surface(self.screen.get_size()).convert()
		self.obstacle = obstacle.Obstacle()
		self.spaceship = spaceship.SpaceShip(50,50,'')
		self.sprites = pygame.sprite.RenderPlain((spaceship,obstacle))	#setup main menue, as well as other objects

	def mainloop(self):

		#Setup Screen, Spaceship
	
		#Start Timer

		pygame.key.set_repeat(1,50)
		GameExit = False
		while not GameExit:	#main loop, a single frame

			#Setup first Obstacles


			#check for events/user input
			for event in pygame.event.get():
				if event == pygame.QUIT:
					GameExit = True
				if event == pygame.KEYDOWN:
					self.spaceship.move(event.key)

			self.screen.update(self.sprites)
			
			pygame.display.flip()

			#react to user input/update models

			#process updates / animations

			#redraw GUI / frame


def main():
	game = Controller()
	game.mainloop()
main()

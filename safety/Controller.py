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
import pigame
import Obstacle
import SpaceShip
import Screen

SCREEN_CENTER = (0,0)
class Controller:
	"""Main clas of game, all actions occure in this class"""

	def __init__(self)
		#setup main menue, as well as other objects

	def mainloop(self):

		#Setup Screen, Spaceship
	
		#Start Timer
	
		while(True):	#main loop, a single frame

			#Setup first Obstacles


			#check for events/user input
			

			#react to user input/update models

			#process updates / animations

			#redraw GUI / frame


def main():
	game = Controller()
	game.mainloop()
main()

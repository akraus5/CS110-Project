import time
import pigame
import obstacle
import spaceShip
import screen

SCREEN_CENTER = (0,0)
class Controller:
	"""Main class of game, all actions occure in this class"""

	def __init__(self)	#screen setup
		pygame.init()
		#setup main menue, as well as other objects, width, height, screen, background, ship, objects, sprites

	def main_menue(self):
		gameStart = False
		while (not gameStart:)
			#Screen setup, menue
			window = screen.Screen()
			#main menue GUI
			
			#Possibel options or difficulty

	def mainloop(self):
		#Setup Screen, Spaceship
		#Start Timer
		gameStart = time.Time()
		George = spaceShip.SpaceShip()
		while(bool(George)):	#main loop, a single frame

			#Setup first Obstacles


			#check for events/user input
			

			#react to user input/update models
			#screen.frameChange()
			#process updates / animations

			#redraw GUI / frame
		window.endgame(bool(George))
		quit()

	def inputs(self, lk, rk)#left key and right key
		self.lk = lk
		self.rk = rk
		evt = python.event.get()
			if (evt == self.lk):
				#move left
				George.move(1,0):
			elif(evt == self.rk):
				#move right
				George.move(0,1):

		
def main():
	game = Controller()
	game.mainloop()
main()

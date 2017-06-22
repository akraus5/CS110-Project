import time
import pygame
import obstacle
import spaceship
import resup

class Controller:
	"""Main clas of game, all actions occure in this class"""

	def __init__(self,scrW,scrH)
		pygame.init()
		#self.screen = screen.Screen()	#later
		self.scrW = scrW
		self.scrH = scrH
		self.gameDisplay = pygame.display.set_mode((scrW,scrH))
		self.background = pygame.Surface(self.screen.get_size()).convert()
		self.obstacle = obstacle.Obstacle(self.scrW/2,self.scrH/2,self.scrW,self.scrH)
		self.spaceship = spaceship.SpaceShip(self.scrW,self.scrH)
		self.resup = resup.Resup((self.scrwid // 2) - (self.shipW // 2) , ((self.scrht * 1) // 7) - (self.shipH // 2))
		self.sprites = pygame.sprite.RenderPlain((self.spaceship,self.obstacle,self.resup))	#setup main menue, as well as other objects
		pygame.display.set_caption('Game')

	def mainloop(self):
		black = (0,0,0)
		
		#Start Timer
		
		pygame.key.set_repeat(1,50)
		GameExit = False
		while not GameExit:	
			self.background.fill(black)

			#check for events/user input
			for event in pygame.event.get():
				if event == pygame.QUIT:
					GameExit = True
				if event == pygame.KEYDOWN:
					self.spaceship.move(event.key)
			
			self.obstacle.move()
			self.obstacle.change_dir()

			if pygame.sprite.collide_rect(self.spacehsip,self.obstacle):
				self.spaceship.die()
			if pygame.sprite.collide_rect(self.spacehsip,self.resup):
				self.spaceship.winLev()
				
			self.gameDisplay.blit(self.background,(0,0))
			self.sprites.draw(self.gameDisplay)

			pygame.display.flip()

			#react to user input/update models

			#process updates / animations

			#redraw GUI / frame


def main():
	game = Controller(500,500)
	game.mainloop()
main()

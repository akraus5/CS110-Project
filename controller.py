#import time
import obstacle,spaceship,resup
import pygame

class Controller:
	"""Main clas of game, all actions occure in this class"""

	def __init__(self,scrW,scrH):
		pygame.init()
		#self.screen = screen.Screen()	#later
		self.scrW = scrW
		self.scrH = scrH
		self.gameDisplay = pygame.display.set_mode((scrW,scrH))
		self.background = pygame.Surface(self.gameDisplay.get_size()).convert()
		self.obstacle = obstacle.Obstacle(self.scrW/2,self.scrH/2,self.scrW,self.scrH,'right',5)
		self.spaceship = spaceship.SpaceShip(self.scrW,self.scrH,5)
		self.resup = resup.Resup((self.scrW // 2) , ((self.scrH * 1) // 7))
		self.sprites = pygame.sprite.RenderPlain((self.spaceship,self.obstacle,self.resup))	#setup main menue, as well as other objects
		pygame.display.set_caption('Game')

	def message_to_screen(self,text,color,size,font,position=0):
		self.font = pygame.font.SysFont(font,size)
		self.color = color
		self.position = position
		self.text = self.font.render(text,True,self.color)
		self.textRect = self.text.get_rect()
		self.textRect.center = (self.scrW/2,self.scrH/2+self.position)
		self.gameDisplay.blit(self.text,self.textRect)
		pygame.display.flip()

	def mainloop(self):
		black = (0,0,0)
		red = (255,0,0)
		#Start Timer

		pygame.key.set_repeat(1,50)
		GameExit = False
		GameLose = False
		while not GameExit:
			while GameLose == Flase:
				self.background.fill(black)

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						GameExit = True
					if event.type == pygame.KEYDOWN:
						self.spaceship.move(event.key)

				self.obstacle.move()
				self.obstacle.change_dir()

				if pygame.sprite.collide_rect(self.spaceship,self.obstacle):
					self.spaceship.die()
				if pygame.sprite.collide_rect(self.spaceship,self.resup):
					self.spaceship.winLev()

				self.gameDisplay.blit(self.background,(0,0))
				self.sprites.draw(self.gameDisplay)

				pygame.display.flip()

				alive,win = self.spaceship.getStatus()

				if not alive:
					GameLose = True
			if GameLose == True:	
				self.background.fill(black)
				self.message_to_screen('You Lose',red,100,'comicsansms')
				self.message_to_screen('Press C to play again or Q to quit',black,70,'comicsansms',30)
				
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						GameExit = True
					if event.type == pygame.KEYDOWN:
						if event.key = pygame.K_q:
							GameExit = True
							GameLose = False
						if event.key = pygame.K_c:
							self.mainloop()




def main():
	game = Controller(500,500)
	game.mainloop()
main()

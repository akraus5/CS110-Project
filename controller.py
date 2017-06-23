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
		self.level = 1
		self.gameDisplay = pygame.display.set_mode((scrW,scrH))
		self.background = pygame.Surface(self.gameDisplay.get_size()).convert()
		self.initializeObjects()

		pygame.display.set_caption('Game')

	def initializeObjects(self):
		self.obstacle = obstacle.Obstacle(self.scrW/2,self.scrH/2,self.scrW,self.scrH,'right',5)
		self.spaceship = spaceship.SpaceShip(self.scrW,self.scrH,5)
		self.resup = resup.Resup((self.scrW // 2) , ((self.scrH * 1) // 7))
		self.sprites = pygame.sprite.RenderPlain((self.spaceship,self.obstacle,self.resup))	#setup main menue, as well as other objects

	def message_to_screen(self,text,color,size,font,position=0):
		self.font = pygame.font.SysFont(font,size)
		self.color = color
		self.position = position
		self.text = self.font.render(text,True,self.color)
		self.textRect = self.text.get_rect()
		self.textRect.center = (self.scrW/2,self.scrH/2+self.position)
		self.gameDisplay.blit(self.text,self.textRect)
		pygame.display.flip()

	def press_c_message(self):
		self.background.fill(black)

		if self.level == 1
			text = "You are tired from your journey\n do you go to sleep or a party?\n Press 1 to sleep, 2 to party"

		self.message_to_screen(text,red,10,'comicsansms')
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					self.initializeObjects()
					GameLose = False
				if event.key == pygame.K_2:
					self.initializeObjects()
					GameLose = False
		

	def mainloop(self):
		black = (0,0,0)
		red = (255,0,0)
		white = (255,255,255)
		#Start Timer

		pygame.key.set_repeat(1,50)
		GameExit = False
		GameLose = False
		GameWin = False
		while not GameExit:
			while GameLose == False and GameExit == False:
				self.background.fill(black)

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						GameExit = True
					if event.type == pygame.KEYDOWN:
						self.spaceship.move(event.key)
				#	elif:
				#		event.type != pygame.KEYDOWN:
				#		self.spaceship.move()
							

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
				if win:
					GameWin = True
			if GameLose:
				self.message_to_screen('You Lose',red,100,'comicsansms')
				self.message_to_screen('Press C to play again or Q to quit',white,30,'comicsansms',70)

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						GameExit = True
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_q:
							GameExit = True
						if event.key == pygame.K_c:
							self.initializeObjects()
							GameLose = False
			if GameWin:
				self.message_to_screen('You Win',red,100,'comicsansms')
				self.message_to_screen('Press C to play again or Q to quit',white,30,'comicsansms',70)

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						GameExit = True
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_q:
							GameExit = True
						if event.key == pygame.K_c:
							self.message_to_screen('You Lose',red,100,'comicsansms')
							self.initializeObjects()
							GameWin = False





def main():
	game = Controller(500,500)
	game.mainloop()
main()

#import time
import obstacle,spaceship,resup
import pygame

BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)

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
		self.obstacle = obstacle.Obstacle(self.scrW/2,self.scrH/2,self.scrW,self.scrH,'right')
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

	def LoseWinMessage(self):
		if self.GameLose:
			self.message_to_screen('You Lose',RED,100,'comicsansms')
			self.message_to_screen('Press C to play again or Q to quit',WHITE,30,'comicsansms',70)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.GameExit = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						self.GameExit = True
					if event.key == pygame.K_c:
						self.initializeObjects()
						self.GameLose = False
		if self.GameWin:
			self.message_to_screen('You Win',RED,100,'comicsansms')
			self.message_to_screen('Press C to play again or Q to quit',WHITE,30,'comicsansms',70)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.GameExit = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						self.GameExit = True
					if event.key == pygame.K_c:
						self.press_c_message()
						if event.key == pygame.K_1:
							self.initializeObjects()
							self.GameLose = False
						if event.key == pygame.K_2:
							self.initializeObjects()
							self.GameLose = False



	def press_c_message(self):
		self.gameDisplay.fill(BLACK)
		self.gameDisplay.blit(self.background,(0,0))
		pygame.display.flip()

		if self.level == 1:
			text = "You are tired from your journey\n do you go to sleep or a party?\n Press 1 to sleep, 2 to party"

		self.message_to_screen(text,RED,15,'comicsansms')
		'''
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					self.GameExit = True
				if event.key == pygame.K_1:
					self.initializeObjects()
					self.GameLose = False
				if event.key == pygame.K_2:
					self.initializeObjects()
					self.GameLose = False
		'''

	def mainloop(self):
		#Start Timer

		pygame.key.set_repeat(1,50)
		self.GameExit = False
		self.GameLose = False
		self.GameWin = False
		while not self.GameExit:
			while self.GameLose == False and self.GameWin == False and self.GameExit == False:
				self.background.fill(BLACK)

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						self.GameExit = True
					if event.type == pygame.KEYDOWN:
						self.spaceship.move(event.key)
				self.spaceship.move()


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
					self.GameLose = True
				if win:
					self.GameWin = True

			self.LoseWinMessage()



def main():
	game = Controller(500,500)
	game.mainloop()
main()

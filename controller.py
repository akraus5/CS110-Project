#import time
import obstacle,spaceship,resup
#import levelpack
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
		self.firstMessage = True
		self.gameDisplay = pygame.display.set_mode((scrW,scrH))
		self.background = pygame.Surface(self.gameDisplay.get_size()).convert()
		self.initializeObjects()

		pygame.display.set_caption('Game')

	def initializeObjects(self):
		self.obstacle = obstacle.Obstacle(self.scrW/2,self.scrH/2,self.scrW,self.scrH,'right')
		self.spaceship = spaceship.SpaceShip(self.scrW,self.scrH,5)
		self.resup = resup.Resup((self.scrW // 2) , ((self.scrH * 1) // 7))
		self.sprites = pygame.sprite.RenderPlain((self.spaceship,self.obstacle,self.resup))	#setup main menue, as well as other objects

	def message_to_screen(self,txtlis,color,size,font,pos=0,bold=False):
		font = pygame.font.SysFont(font,size)
		font.set_bold(bold)
		color = color
		position = pos

		indent = 0

		for i in range(len(txtlis)):
			text = font.render(txtlis[i],True,color)
			textRect = text.get_rect()
			textRect.center = (self.scrW/2,self.scrH/2+pos+indent)
			self.gameDisplay.blit(text,textRect)
			indent += size+10
		#pygame.display.flip()

	def LoseWinMessage(self):
		if self.GameLose:
			self.message_to_screen(['You Lose'],RED,100,'comicsansms')
			self.message_to_screen(['Press C to play again or Q to quit'],WHITE,30,'comicsansms',70)

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
			if self.firstMessage:
				self.message_to_screen(['You Win'],RED,100,'comicsansms')
				self.message_to_screen(['Press C to continue or Q to quit'],WHITE,30,'comicsansms',70)

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						self.GameExit = True
					if event.type == pygame.KEYDOWN:
						if event.type == pygame.QUIT:
							self.GameExit = True
						if event.key == pygame.K_q:
							self.GameExit = True
						if event.key == pygame.K_c:
							self.firstMessage = False
							#self.press_c_message()

			else:
				self.gameDisplay.fill(BLACK)
				self.gameDisplay.blit(self.background,(0,0))

				if self.level == 1:
					text1 = "You are exhausted from your journey, but some of your"
					text2 = "friends are throwing a party. Do you goto the party, or"
					text3 = "stay in for the night?"
					text4 = "Press 1 to go to party, press 2 to head to sleep"
					text5 = "Q to quit"
					self.message_to_screen([text1,text2,text3,text4,text5],WHITE,25,'orcastd')

				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_q:
							self.GameExit = True
						if event.key == pygame.K_1:
							self.initializeObjects()
							self.GameWin = False
							self.firstMessage = True
							#self.level += 1
						if event.key == pygame.K_2:
							self.initializeObjects()
							self.GameWin = False
							self.firstMessage = True
							#self.level += 1

		pygame.display.flip()

	def mainloop(self):
		#Start Timer

		pygame.key.set_repeat(1,50)
		self.GameExit = False
		self.GameLose = False
		self.GameWin = False

		while not self.GameExit:

			while not (self.GameLose or self.GameWin or self.GameExit):
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

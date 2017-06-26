#import time
import obstacle,spaceship,resup
#import levelpack
import pygame
import random

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
		self.level = 0
		self.firstMessage = False
		self.gameDisplay = pygame.display.set_mode((scrW,scrH))
		self.background = pygame.Surface(self.gameDisplay.get_size()).convert()
		self.initializeObjects()

		pygame.display.set_caption('Space Travel')

	def initializeObjects(self, numobs=1):
		self.spaceship = spaceship.SpaceShip(self.scrW,self.scrH,5)
		self.resup = resup.Resup((self.scrW // 2) , ((self.scrH * 1) // 7))

		self.obstacle = []
		for i in range(numobs):
			posx = self.scrW/2
			posy = self.scrH/2

			mydir = random.choice(['left','right','up','down'])

			self.obstacle.append(obstacle.Obstacle(posx,posy,self.scrW,self.scrH,mydir))

		self.sprites = pygame.sprite.RenderPlain((self.spaceship,)+tuple(self.obstacle)+(self.resup,))	#setup main menue, as well as other objects
	'''
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
	'''
	'''
	def message_to_screen(self,par,color,size,font,position=0,bold=False):
		font = pygame.font.SysFont(font,size)
		font.set_bold(bold)
		#color = color
		#position = pos
		my_lines = []

		#testtext = font.render("test",True,color)
		matric = font.metrics('@')[0]
		width = matric[4]

		max_len = self.scrW // width

		size = 0
		lines = []
		line = ""
		prev_str = ""
		for ch in par:
			temp_line = line + prev_str

			if ch == ' ':
				if len(temp_line)+1 < max_len: # +1 to account for preceding space
					line += ' ' + prev_str
				else:
					lines.append(line)
					line = ' ' + prev_str
				prev_str = ""
			else:
				prev_str += ch

		parHeight = (font.get_linesize()) * len(lines)

		for i in range(len(lines)):
			text = font.render(lines[i],True,color)
			textRect = text.get_rect()

			textRect.x = self.scrW//2 - textRect.width//2
			textRect.y = self.scrH//2 - textRect.height//2 - parHeight//2
			#textRect.center = (self.scrW/2,self.scrH/2+position)
			self.gameDisplay.blit(text,textRect)
			parHeight -= (font.get_linesize())
			#position += font.get_linesize()
	'''

	# Source of message_to_screen() code: http://pygame.org/wiki/TextWrap
	# draw some text into an area of a surface
	# automatically wraps words
	# returns any text that didn't get blitted
	def message_to_screen(self,text, color, sz, fnt, disp=0, aa=True, bkg=None):
		rect=self.gameDisplay.get_rect()
		rect.width -= (.25 * self.scrW)
		rect.height -= (.25 * self.scrH)
		rect.center = (self.scrW/2,self.scrH/2 + disp)

		font = pygame.font.SysFont(fnt,sz)
		#rect = Rect(rect)
		y = rect.top
		lineSpacing = 2

	    # get the height of the font
		fontHeight = font.size("Tg")[1]

		while text:
			i = 1

	        # determine if the row of text will be outside our area
			if y + fontHeight > rect.bottom:
				break

	        # determine maximum width of line
			while font.size(text[:i])[0] < rect.width and i < len(text):
				i += 1

	        # if we've wrapped the text, then adjust the wrap to the last word
			if i < len(text):
				i = text.rfind(" ", 0, i) + 1

	        # render the line and blit it to the surface
			if bkg:
				image = font.render(text[:i], 1, color, bkg)
				image.set_colorkey(bkg)
			else:
				image = font.render(text[:i], aa, color)

			self.gameDisplay.blit(image, (rect.left, y))
			y += fontHeight + lineSpacing

	        # remove the text we just blitted
			text = text[i:]

		return text


	def LoseWinMessage(self):
		if self.GameLose:
			self.message_to_screen('You Lose',RED,100,'comicsansms')
			self.message_to_screen('Press C to play again or Q to quit',WHITE,30,'comicsansms',200)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.GameExit = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						self.GameExit = True
					if event.key == pygame.K_c:
						self.initializeObjects()
						self.GameLose = False
						self.level = 0
						self.GameWin = True
						self.firstMessage = False
		elif self.GameWin:
			if self.firstMessage:
				self.message_to_screen('You Win',RED,100,'comicsansms')
				self.message_to_screen('Press C to continue or Q to quit',WHITE,30,'comicsansms',200)

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

			else:
				self.gameDisplay.fill(BLACK)
				self.gameDisplay.blit(self.background,(0,0))

				if self.level == 0:
					text = "Welcome traveller. Your mission is about to begin. You are headed to the Far Colony, the furthest human outreach "
					text += "post from Earth, to help the colony advance their transgalactic Warp Drive capabilities. The Far Colony is located far beyond "
					text += "the edge of our solar system. You do not have enough food or supplies to make it there in one shot. Lucky for you, there "
					text += "are several resupply locations on the route. Your ship launches tomorrow. Do you accept [1] or deny [2] the mission?"
					self.message_to_screen(text,WHITE,25,'orcastd')

				elif self.level == 1:
					text = "You are exhausted from your journey, but some of your "
					text += "friends are throwing a party. Do you go to the party, or "
					text += "stay in for the night? "
					text += "Press 1 to go to party, press 2 to head to sleep. "
					text += "Q to quit"
					self.message_to_screen(text,WHITE,25,'orcastd')

				elif self.level == 2:
					text = "You have finally made it to the Curiosity Center of Mars. You are ready to start "
					text += "resupplying your ship with fuel, food, and water, when a message is displayed on your ship's dashboard. The message "
					text += "reads 'Warning: Water may contain R. horus, a bacterial species of Mars origin. Without proper filtration, "
					text += "the water may be toxic. Select a filtration method: activated carbon [1] or coagulation [2]'"
					text += "                                 Which will you choose?"
					self.message_to_screen(text,WHITE,25,'orcastd')

				elif self.level == 3:
					text = "Jupiter"

				else: # temporary else statement
					text = "Keep up the good work! Press 1 or 2 to continue."
					self.message_to_screen(text,WHITE,25,'orcastd')


				'''
				elif self.level == 2:
					#level 2 text
				elif self.level ==3:
					#level 3 text
				elif self.level ==4:
					#level 4 text
				'''

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						self.GameExit = True
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_q:
							self.GameExit = True
						if event.key == pygame.K_1:
							self.level += 1
							self.initializeObjects(self.level)
							self.GameWin = False
							self.firstMessage = True
						if event.key == pygame.K_2:
							if self.level == 0:
								self.GameExit = True
							else:
								self.level += 1
								self.initializeObjects(self.level)
								self.GameWin = False
								self.firstMessage = True

		pygame.display.flip()

	def mainloop(self):
		#Start Timer

		pygame.key.set_repeat(1,50)
		self.GameExit = False
		self.GameLose = False
		self.GameWin = True

		while not self.GameExit:

			while not (self.GameLose or self.GameWin or self.GameExit):
				self.background.fill(BLACK)

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						self.GameExit = True
					if event.type == pygame.KEYDOWN:
						self.spaceship.move(event.key)
				self.spaceship.move()

				for i in range(len(self.obstacle)):
					self.obstacle[i].move()
					self.obstacle[i].change_dir()

					if pygame.sprite.collide_rect(self.spaceship,self.obstacle[i]):
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
					self.firstMessage = True


			self.LoseWinMessage()



def main():
	game = Controller(500,500)
	game.mainloop()
main()

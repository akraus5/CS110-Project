#import time
import obstacle,spaceship,resup
#import levelpack
import pygame
import random

BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)

WIDTH = 500
HEIGHT = 1000

class Controller:
	"""Main clas of game, all actions occure in this class"""

	def __init__(self):
		pygame.init()
		self.level = 0
		self.gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
		self.background = pygame.Surface(self.gameDisplay.get_size()).convert()
		self.initializeObjects()

		pygame.display.set_caption('Space Travel')

	def initializeObjects(self, numobs=1):
		self.spaceship = spaceship.SpaceShip(5)
		self.resup = resup.Resup(WIDTH/ 2 , (HEIGHT* 1) // 7))

		self.obstacle = []
		for i in range(numobs):
			posx = WIDTH/2
			posy = HEIGHT/2

			mydir = random.choice(['left','right','up','down'])

			self.obstacle.append(obstacle.Obstacle(posx,posy,WIDTH,HEIGHT,mydir))

		self.sprites = pygame.sprite.group(self.spaceship, self.obstacle, self.resup)	#setup main menue, as well as other objects
	
	# Source of message_to_screen() code: http://pygame.org/wiki/TextWrap
	# draw some text into an area of a surface
	# automatically wraps words
	# returns any text that didn't get blitted
	def message_to_screen(self,text, color, sz, fnt, disp=0, aa=True, bkg=None):
		rect=self.gameDisplay.get_rect()
		rect.width -= (.25 * WIDTH)
		rect.height -= (.25 * HEIGHT)
		rect.center = (WIDTH/2,HIGHT/2 + disp)

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

	def press_cORq(self):
	    self.waiting = True
	    while self.waiting:
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		          pygame.quit()
		          quit()
		    if event.type == pygame.KEYDOWN:
		        if event.key == pygame.K_q:
		            pygame.quit()
		            quit()
		        elif event.key == pygame.K_c:
		            self.waiting = False

	def game_over_screen(self):
		self.gameDisplay.fill(BLACK)
		self.message_to_screen('You Lose',RED,100,'comicsansms')
		self.message_to_screen('Press C to play again or Q to quit',WHITE,30,'comicsansms',200)
		pygame.display.flip()

		self.press_cORq()

	def game_win_screen(self):
		self.gameDisplay.fill(BLACK)
		self.message_to_screen('You Win','comicsansms',RED,100)
		self.message_to_screen('Press C to continue or Q to quit','comicsansms',WHITE,30,250)

		self.press_cORq()

		self.gameDisplay.fill(BLACK)
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
			elf.message_to_screen(text,WHITE,25,'orcastd')

		self.waiting = True
		while self.waiting:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()
						quit()
					elif event.key == pygame.K_1:
						self.level += 1
						self.initializeObjects(self.level)
						self.waiting = False
					elif event.key == pygame.K_2:
						if self.level == 0:
							self.GameExit = True
						else:
							self.level += 1
							self.initializeObjects(self.level)
							self.waiting = False
	def mainloop():
	# Game loop
		gameExit = False
		gameOver = False
		gameWin = False
		while not gameExit:
		    if gameOver:
			game_over_screen()
			self.initializeObejcts()
			gameOver = False
				          
		    elif gameWin:
			game_win_screen()
			gameWin = False
				           
		    # Keep loop running at the right speed
		    #clock.tick(FPS)

		    # Process input
		    for event in pygame.event.get():
			if event.type == pygame.QUIT:
			    gameExit = True

		    # Update
		    self.all_sprites.update()

		    # Check to see if the spaceship hit an obstacle
		    if pygame.sprite.collide_rect(self.spaceship,self.obstacle):
			gameOver = True

		    # Check to see if the spaceship hit the resup
		    elif pygame.sprite.collide_rect(self.spaceship,self.resup):
			gameWin = True
				           
		    # Draw
		    self.gameDisplay.fill(BLACK)
		    self.all_sprites.draw(gameDisplay)


		    pygame.display.flip()



		pygame.quit()
		quit()



def main():
	game = Controller(500,500)
	game.mainloop()
main()

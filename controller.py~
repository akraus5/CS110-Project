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

	def __init__(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.width = 500
		self.height= 700
		self.level = 1
		self.gameDisplay = pygame.display.set_mode((self.width,self.height))
		self.background = pygame.Surface(self.gameDisplay.get_size()).convert()
		self.initializeObjects()

		pygame.display.set_caption('Space Travel')

	def initializeObjects(self, numobs=1,notReverse = True):
		self.spaceship = spaceship.SpaceShip(self.width, self.height,5)
		self.spaceship.change_lucid(notReverse)

		img = ''
		direction = random.choice(['right','left'])
		if self.level == 1:
			img = 'moon'
			self.resup = resup.Resup(self.width/2, self.height/7,self.width,self.height,img)
		elif self.level == 2:
			img = 'mars'
			self.resup = resup.Resup(self.width/2, self.height/7,self.width,self.height,img,True,direction)
		elif self.level == 3:
			img = 'POD_small'
			self.resup = resup.Resup(self.width/2, self.height/7,self.width,self.height,img,True,direction,2)
		else:
			img = 'satellite'
			self.resup = resup.Resup(self.width/2, self.height/7,self.width,self.height,img,True,direction,3)


		self.obstacle = []
		for i in range(numobs):
			posx = random.randrange(0,self.width)
			posy = random.randrange(self.resup.rect.bottom,self.spaceship.rect.top)

			mydirx = random.choice(['left','right',None])
			mydiry = random.choice(['up',None])			

			self.obstacle.append(obstacle.Obstacle(posx,posy,self.width,self.height,mydirx,mydiry))

			posx = random.randrange(0,self.width-self.obstacle[i].rect.width)
			posy = random.randrange(self.resup.rect.bottom,self.spaceship.rect.top-self.obstacle[i].rect.height)

			self.obstacle[i].setX(posx)
			self.obstacle[i].setY(posy)

		self.sprites = pygame.sprite.RenderPlain((self.spaceship,) + tuple(self.obstacle)+ (self.resup,))	#setup main menue, as well as other objects

	# Source of message_to_screen() code: http://pygame.org/wiki/TextWrap
	# draw some text into an area of a surface
	# automatically wraps words
	# returns any text that didn't get blitted
	def message_to_screen(self,text, color, sz, fnt, disp=0, aa=True, bkg=None):
		rect=self.gameDisplay.get_rect()
		rect.width -= (.25 * self.width)
		rect.height -= (.25 * self.height)
		rect.center = (self.width/2,self.height/2 + disp)

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
		pygame.key.set_repeat(1,50)
		waiting = True
		while waiting:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()
						quit()
					elif event.key == pygame.K_c:
						waiting = False
	def intro_screen(self):
		
		self.gameDisplay.fill(BLACK)

		text = "Welcome traveller. Your mission is about to begin. You are headed to the Far Colony, the furthest human outreach "
		text += "post from Earth, to help the colony advance their transgalactic Warp Drive capabilities. The Far Colony is located far beyond "
		text += "the edge of our solar system. You do not have enough food or supplies to make it there in one shot. Lucky for you, there "
		text += "are several resupply locations on the route. Your ship launches tomorrow. Do you accept [C] or deny [Q] the mission?"

		self.message_to_screen(text,WHITE,25,'orcastd')
		pygame.display.flip()

		self.press_cORq()


	def game_over_screen(self):
		self.gameDisplay.fill(BLACK)
		self.message_to_screen('You Lose',RED,100,'comicsansms')
		self.message_to_screen('Press C to play again or Q to quit',WHITE,30,'comicsansms',200)
		pygame.display.flip()

		self.press_cORq()

	def game_win_screen(self):

		self.gameDisplay.fill(BLACK)
		self.message_to_screen('You Win',RED,100,'comicsansms')
		self.message_to_screen('Press C to continue or Q to quit',WHITE,30,'comicsansms',250)
		pygame.display.flip()

		self.press_cORq()

		self.gameDisplay.fill(BLACK)
		if self.level == 1:
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
			text = "The POD was the first checkpoint satellite in our solar system. All ships are required to dock to the POD and get approval before passing Jupiter. However, when I told the POD authorities that I am being sent on a mission to the Far Colony, they laugh and say that there are no outreach posts beyond the POD. I knew that the Far Colony was a top secret research base, but I did not know that even the POD authorities were not aware of its existence. I can either try contacting my boss back on Earth for help, but through unencrypted channels [1], or leave the POD and risk continuing past Jupiter without detection [2]."
			self.message_to_screen(text,WHITE,25,'orcastd')

		else: # temporary else statement
			text = "Keep up the good work! Press 1 or 2 to continue."
			self.message_to_screen(text,WHITE,25,'orcastd')

		pygame.display.flip()

		waiting = True
		while waiting:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()
						quit()
					elif event.key == pygame.K_1:
						if self.level == 1:
							notReverse = False
						if self.level == 2:
							notReverse = True
						if self.level == 3:
							notReverse = True
						self.level += 1
						self.initializeObjects(self.level,notReverse)
						waiting = False
					elif event.key == pygame.K_2:
						if self.level == 1:
							notReverse = True
						if self.level == 2:
							notReverse = False
						if self.level == 3:
							notReverse = False
						self.level += 1
						self.initializeObjects(self.level,notReverse)
						waiting = False

	def mainloop(self):
	# Game loop
		self.intro_screen()
		gameExit = False
		gameOver = False
		gameWin = False
		pygame.key.set_repeat(1,50)
		while not gameExit:
			self.clock.tick(60)
			if gameOver:
				self.game_over_screen()
				self.level = 1
				self.initializeObjects(self.level)
				self.intro_screen()
				gameOver = False

			elif gameWin:
				self.game_win_screen()
				gameWin = False

		    # Keep loop running at the right speed
		    #clock.tick(FPS)

		    # Process input
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True

		    # Update
			self.sprites.update()

		    # Check to see if the spaceship hit an obstacle
			for i in range(len(self.obstacle)):
				if pygame.sprite.collide_rect(self.spaceship,self.obstacle[i]):
					gameOver = True
				col = (pygame.sprite.collide_rect(self.resup,self.obstacle[i]))
				self.obstacle[i].change_dir(col)
				self.resup.change_dir(col)
		    # Check to see if the spaceship hit the resup
			if pygame.sprite.collide_rect(self.spaceship,self.resup):
				gameWin = True

		    # Draw
			self.gameDisplay.fill(BLACK)
			self.sprites.draw(self.gameDisplay)


			pygame.display.flip()

		pygame.quit()
		quit()



def main():
	game = Controller()
	game.mainloop()
main()

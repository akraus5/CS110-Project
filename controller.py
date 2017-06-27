#import time
import obstacle,spaceship,resup
#import levelpack
import pygame
import json
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
		self.notReverse = True
		self.gameDisplay = pygame.display.set_mode((self.width,self.height))
		self.background = pygame.Surface(self.gameDisplay.get_size()).convert()
		self.initializeObjects()
		
		try:
			ptr= open('story.json','r')
			self.story = json.loads(ptr.read())
		except:
			print('Cannot find the file')
		else:
			ptr.close()

		pygame.display.set_caption('Space Travel')

	def initializeObjects(self):
		self.spaceship = spaceship.SpaceShip(self.width, self.height,5)
		self.spaceship.change_lucid(self.notReverse)
		numobs = self.level

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
			posx = 0
			posy = 0

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

		self.message_to_screen(self.story['start'],WHITE,25,'orcastd')
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
			self.message_to_screen(self.story['lev1'],WHITE,25,'orcastd')

		elif self.level == 2:
			self.message_to_screen(self.story['lev2'],WHITE,25,'orcastd')

		elif self.level == 3:
			self.message_to_screen(self.story['lev3'],WHITE,25,'orcastd')
		elif self.level == 4:
			self.message_to_screen(self.story['fin'],WHITE,25,'orcastd')
		pygame.display.flip()
	
		waiting = True
		pygame.key.set_repeat(1,50)
		while waiting:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()
						quit()
					if event.key == pygame.K_c:
						if self.level == 4:
							waiting = False
					elif event.key == pygame.K_1:
						if self.level == 1:
							self.notReverse = False
						if self.level == 2:
							self.notReverse = True
						if self.level == 3:
							self.notReverse = True
						if self.level!=4:
							waiting = False
					elif event.key == pygame.K_2:
						if self.level == 1:
							self.notReverse = True
						if self.level == 2:
							self.notReverse = False
						if self.level == 3:
							self.notReverse = False
						if self.level!=4:
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
				self.initializeObjects()
				self.intro_screen()
				gameOver = False

			elif gameWin:
				self.game_win_screen()
				gameWin = False
				if self.level ==4:
					self.level = 1
					self.initializeObjects()
					self.intro_screen()
				else:
					self.level += 1
					self.initializeObjects()


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
				if col:
					if (self.resup.rect.bottom > self.obstacle[i].rect.top):
						self.resup.change_dir(col, self.obstacle[i].dirx)
					self.obstacle[i].change_dir(col)
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

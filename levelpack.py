


def level1():
	'''
		To Be Edited, used for levels, called from main loop in controller.



	while not GameExit:	#Demo game, to be modified
		self.background.fill(black)

			#check for events/user input
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

			if((not alive) or win):
				GameExit = True
	'''

def level2():


def level3():


def level4():

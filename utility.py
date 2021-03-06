import os
import pygame

def LoadImage(name, colorkey=None):
	'''
		Load an image
		args: 	name: str, filename
				colorkey: tuple, (R,G,B)
		return: (image,image.get_rect()) - tuple

				image: surface
				image.get_rect(): rect
	'''
	fullname = os.path.join('assets', name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error as message:
		print('Cannot load image:', name)
		raise SystemExit(message)
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey)
	return image, image.get_rect()

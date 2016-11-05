import pygame, math, random, sys
from pygame.locals import *

class Mosquitoe(pygame.sprite.Sprite):
    "Returns: mosquitoe object"
    "Function: update, new_pos"
    "Atributes: area, vector"

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('mosquitoe.png')
        self.area = screen.get_rect()
        self.vector = vector

	def update(self):
		self.rect = self.new_pos(self.rect,self.vector)

	def new_pos(self, rect, vector):
		(angle,z) = vector
		(dx,dy) = (z*math.cos(angle),z*math.sin(angle))
		return rect.move(dx,dy)


"Screen"
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('GANN')

"Fill background"
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

"Blit everything to the screen"
screen.blit(background, (0, 0))
pygame.display.flip()

"Init clock"
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
    "60 fps"
    clock.tick(60)

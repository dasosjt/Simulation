import pygame, math, random, sys
from pygame.locals import *

class Mosquitoe(pygame.sprite.Sprite):
    "Returns: mosquitoe object"
    "Function: update, new_pos"
    "Atributes: vector"

    def __init__(self, vector, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image = self.image.convert()
        self.image.fill((20,20,20))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y  = position
        self.vector = vector

	def update(self):
		self.rect = self.new_pos(self.rect, self.vector)

	def new_pos(self, rect, vector):
		(angle,z) = vector
		(dx,dy) = (z*math.cos(angle), z*math.sin(angle))
		return rect.move(dx,dy)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


"Screen"
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('GANN')

"Fill background"
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

m1 = Mosquitoe((0.3, 5), (30, 30))

"Init clock"
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()

    screen.blit(background, (0, 0))
    m1.draw(screen)

    "60 fps"
    clock.tick(60)
    pygame.display.update()

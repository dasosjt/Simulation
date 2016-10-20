import pygame
import sys
import numpy as np
from pygame.locals import *


SCREEN_WIDTH = 410
SCREEN_HEIGHT = 615

def get_first_angle((x, y)):
    angle = np.random.uniform(360)
    x1 = 30*np.cos(angle)+x
    y1 = 30*np.sin(angle)+y
    return (x1, y1)

class Player(object):
    def __init__(self):
        self.image = pygame.image.load('player.png')
        self.sprite = self.image.convert_alpha()
        self.x = -self.sprite.get_rect().centerx
        self.y = -self.sprite.get_rect().centery

    def draw(self, surface):
        surface.blit(self.sprite, (self.x, self.y))

    def position(self, x, y):
        self.x =  x-self.sprite.get_rect().centerx
        self.y =  y-self.sprite.get_rect().centery

    def get_center_postion(self):
        return (self.x+self.sprite.get_rect().centerx, self.y+self.sprite.get_rect().centery)


pygame.init()
screen = pygame.display.set_mode((640, 400))

player = Player()
clock = pygame.time.Clock()
player.position(50,50)

first_line = get_first_angle(player.get_center_postion())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255,255,255))
    player.draw(screen)
    pygame.draw.line(screen, (0, 0, 255), player.get_center_postion(), first_line)
    pygame.display.update()

    clock.tick(40)

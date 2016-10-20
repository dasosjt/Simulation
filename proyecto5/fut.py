import pygame
import sys
import numpy as np
from pygame.locals import *
from math import *
import fuzzy_logic as fl


SCREEN_WIDTH = 410
SCREEN_HEIGHT = 615

def get_first_angle((x, y)):
    angle = np.random.uniform(360)
    print angle
    x1 = 25*np.cos(np.deg2rad(angle))+x
    y1 = -25*np.sin(np.deg2rad(angle))+y
    return (x1, y1)

def get_distance_between(object1, object2):
    x = float(object1.get_center_postionx() - object2.get_center_postionx())
    y = float(object1.get_center_postiony() - object2.get_center_postiony())
    z = np.sqrt(np.power(x,2) + np.power(y,2))
    return z

def get_angle_between(object1, object2):
    dx = float(object1.get_center_postionx() - object2.get_center_postionx())
    dy = float(object1.get_center_postiony() - object2.get_center_postiony())
    rads = atan2(-dy,dx)
    rads %= 2*pi
    degs = degrees(rads)
    return degs

class Bit(object):
    def __init__(self, image):
        self.image = pygame.image.load(image)
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

    def get_center_postionx(self):
        return self.x+self.sprite.get_rect().centerx

    def get_center_postiony(self):
        return self.y+self.sprite.get_rect().centery


pygame.init()
screen = pygame.display.set_mode((640, 400))

player = Bit('player.png')
player.position(350,250)

ball = Bit('ball.png')
ball.position(50,250)

clock = pygame.time.Clock()


print get_distance_between(player, ball)
print get_angle_between(ball, player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()

    screen.fill((255,255,255))
    player.draw(screen)
    ball.draw(screen)
    pygame.draw.line(screen, (0, 0, 255), player.get_center_postion(), get_first_angle(player.get_center_postion()))
    pygame.display.update()
    player.x -= fl.move_Horn(get_distance_between(player, ball))
    clock.tick(40)

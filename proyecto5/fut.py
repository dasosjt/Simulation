import pygame
import sys
import numpy as np
from pygame.locals import *
from math import *
import fuzzy_logic as fl


SCREEN_WIDTH = 615
SCREEN_HEIGHT = 410


def update_view_line((x, y), angle):
    x1 = 25*np.cos(np.deg2rad(angle))+x
    y1 = 25*np.sin(np.deg2rad(-angle))+y
    return ((x1, y1), angle)

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

    def set_position(self, x, y):
        dx = self.x+self.sprite.get_rect().centerx + x
        dy = self.y+self.sprite.get_rect().centery + y
        if 0 < dx and dx < SCREEN_WIDTH:
            self.x += x
        if 0 < dy and dy < SCREEN_HEIGHT:
            self.y += y


    def get_center_postion(self):
        return (self.x+self.sprite.get_rect().centerx, self.y+self.sprite.get_rect().centery)

    def get_center_postionx(self):
        return self.x+self.sprite.get_rect().centerx

    def get_center_postiony(self):
        return self.y+self.sprite.get_rect().centery


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

xp = np.random.random_integers(SCREEN_WIDTH, size=(2,))
yp = np.random.random_integers(SCREEN_HEIGHT, size=(2,))

player = Bit('player.png')
player.position(xp[0],yp[0])

ball = Bit('ball.png')
ball.position(xp[1],yp[1])

clock = pygame.time.Clock()

diff_angle = 0
angle = np.random.uniform(0, 360)
angle_between = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
    (view_line, angle) = update_view_line(player.get_center_postion(), angle)
    angle_between = get_angle_between(ball, player)
    diff_angle = angle-angle_between
    #print "\nangle_between \n", angle_between
    #print "\nview angle \n", angle
    print "\ndiff angle \n", diff_angle
    screen.fill((255,255,255))
    player.draw(screen)
    ball.draw(screen)
    pygame.draw.line(screen, (0, 0, 255), player.get_center_postion(), view_line)
    pygame.draw.line(screen, (255, 0, 0), player.get_center_postion(), ball.get_center_postion())
    pygame.display.update()
    move = fl.move_Horn(get_distance_between(player, ball))
    apt = fl.view_Horn(diff_angle)
    angle += apt
    angle %= 360
    player.set_position(move*np.cos(np.deg2rad(angle)), move*np.sin(np.deg2rad(-angle)))
    clock.tick(40)

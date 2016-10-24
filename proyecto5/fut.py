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
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.x = -self.rect.centerx
        self.y = -self.rect.centery

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def position(self, x, y):
        self.x =  x-self.rect.centerx
        self.y =  y-self.rect.centery

    def set_position(self, x, y):
        dx = self.x+self.rect.centerx + x
        dy = self.y+self.rect.centery + y
        if 0 < dx and dx < SCREEN_WIDTH:
            self.x += x
        if 0 < dy and dy < SCREEN_HEIGHT:
            self.y += y

    def get_center_postion(self):
        return (self.x+self.rect.centerx, self.y+self.rect.centery)

    def get_center_postionx(self):
        return self.x+self.rect.centerx

    def get_center_postiony(self):
        return self.y+self.rect.centery


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

xp = np.random.random_integers(SCREEN_WIDTH, size=(2,))
yp = np.random.random_integers(SCREEN_HEIGHT, size=(2,))

player = Bit('player.png')
player.position(xp[0],yp[0])

ball = Bit('ball.png')
ball.position(xp[1],yp[1])

red = Bit('red.png')
red.position(SCREEN_WIDTH-30,SCREEN_HEIGHT/2-10)

bg = Bit('bg.jpg')
bg.position(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

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
                sys.exit()

    view_line = update_view_line(player.get_center_postion(), angle)
    angle_between = get_angle_between(ball, player)
    diff_angle = angle-angle_between
    distance_between = get_distance_between(player, ball)
    distance_between_ball_and_red = get_distance_between(ball, red)

    bg.draw(screen)

    pygame.draw.line(screen, (0, 0, 255), player.get_center_postion(), view_line)
    pygame.draw.line(screen, (255, 0, 0), player.get_center_postion(), ball.get_center_postion())
    pygame.draw.line(screen, (0, 255, 0), player.get_center_postion(), red.get_center_postion())

    player.draw(screen)
    ball.draw(screen)
    red.draw(screen)

    move = fl.move_Horn(distance_between)
    apt = fl.view_Horn(diff_angle)
    angle += apt
    angle %= 360

    if distance_between > 25:
        player.set_position(move*np.cos(np.deg2rad(angle)), move*np.sin(np.deg2rad(-angle)))
    else:
        angle_between_player_and_red = get_angle_between(red, player)
        angle_dest = np.random.uniform(-20, 20)
        f = np.random.uniform(0, 50)
        #print "F ", f
        #print " with angle destv ", angle_dest
        ball.set_position(f*np.cos(np.deg2rad(angle_between_player_and_red+angle_dest)), f*np.sin(np.deg2rad(-angle_between_player_and_red+angle_dest)))

    if distance_between_ball_and_red < 20:
        sys.exit()

    pygame.display.update()
    clock.tick(40)

import pygame, math, random, sys
import numpy as np
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
  "input layer"
  self.input0 = 0
  self.input1 = 0
  self.input2 = 0
  self.input3 = 0
  self.input4 = 0

 def update(self):
  self.rect = self.new_pos(self.rect, self.vector)

 def new_pos(self, rect, vector):
  "Vector with the direction and how much to move"
  (angle, z) = vector
  #print np.rad2deg(angle)
  (dx,dy) = (z*np.cos(angle), -z*np.sin(angle))
  return rect.move(dx,dy)

 def draw(self, surface):
  surface.blit(self.image, (self.rect.x, self.rect.y))

 def angle_between(self, object_to):
  dx = float(self.rect.centerx - object_to.rect.centerx)
  dy = float(self.rect.centery - object_to.rect.centery)
  rads = math.atan2(-dy,dx)
  print np.rad2deg(rads)
  return rads

 def distance_between(self, object_to):
  dx = float(self.rect.centerx - object_to.rect.centerx)
  dy = float(self.rect.centery - object_to.rect.centery)
  z = np.sqrt(np.power(dx,2) + np.power(dy,2))
  return z

 def distance_between_food(self, list_of_food):
  "Reset Input Layer"
  self.input0 = 0
  self.input1 = 0
  self.input2 = 0
  self.input3 = 0
  self.input4 = 0
  for f in list_of_food:
   rads = self.angle_between(f)
   print np.rad2deg(rads)
   if np.rad2deg(rads) < 15 and np.rad2deg(rads) > -15:
    self.input2 = self.distance_between(f)
   elif np.rad2deg(rads) < 35 and np.rad2deg(rads) > 15:
    self.input1 = self.distance_between(f)
   elif np.rad2deg(rads) < 45 and np.rad2deg(rads) > 35:
    self.input0 = self.distance_between(f)
   elif np.rad2deg(rads) < -15 and np.rad2deg(rads) > -35:
    self.input3 = self.distance_between(f)
   elif np.rad2deg(rads) < -35 and np.rad2deg(rads) > -45:
    self.input4 = self.distance_between(f)

"Screen"
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('GANN')

"Fill background"
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

m1 = Mosquitoe((0, 5), (0, 250))
m2 = Mosquitoe((0.5*np.pi, 0), (250, 250))

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
 m1.update()
 m1.draw(screen)
 m2.update()
 m2.draw(screen)
 m2.angle_between(m1)

 "60 fps"
 clock.tick(60)
 pygame.display.update()

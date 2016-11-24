import pygame, math, random, sys
import numpy as np
import random as r
from pygame.locals import *

WIDTH = 640
HEIGHT = 480
MAX_DISTANCE = np.sqrt(np.power(WIDTH, 2) + np.power(HEIGHT, 2))
NODES = 16
INPUT = 2
OUTPUT = 4
SIGMOID = NODES - INPUT - OUTPUT

DP = 10

N_NUMBER_M = 100

CLK = 30

population = np.random.randint(-100,100,(N_NUMBER_M, NODES*NODES))
population = np.multiply(population, 0.01)

def terminar(moscos):
  mayor = 0
  idMayor = 0
  for mosco in moscos:
    print "El fitness del mosco " + str(moscos.index(mosco)) + " es de " + str(mosco.fitness)
    if mosco.fitness > mayor:
      mayor = mosco.fitness
      idMayor = moscos.index(mosco)
  print "El fitness mayor es " + str(mayor) + " del mosco " + str(idMayor)

def sigmoid(number):
  result = 1/(1 + np.exp(-number))
  return result

class Food(pygame.sprite.Sprite):
 "Returns: Food object"
 "Function: draw"

 def __init__(self, position):
  pygame.sprite.Sprite.__init__(self)
  self.image = pygame.Surface([20, 20])
  self.image = self.image.convert()
  self.image.fill((255,0,0))
  self.rect = self.image.get_rect()
  self.rect.x, self.rect.y  = position

 def draw(self, surface):
  surface.blit(self.image, (self.rect.x, self.rect.y))

class Mosquitoe(pygame.sprite.Sprite):
 "Returns: mosquitoe object"
 "Function: update, new_pos"
 "Atributes: vector"

 def __init__(self, vector, position, gann):
  pygame.sprite.Sprite.__init__(self)
  self.image = pygame.Surface([10, 10])
  self.image = self.image.convert()
  self.image.fill((20,20,20))
  self.rect = self.image.get_rect()
  self.rect.x, self.rect.y  = position
  self.vector = vector
  self.fitness = 0
  "GANN"
  self.gann = gann.reshape((NODES, NODES))
  #print self.gann
  "input layer"
  self.input = np.zeros(INPUT)

 def update(self):
  "GANN operations"
  #self.input = np.random.randint(0,MAX_DISTANCE,INPUT)
  self.input[0] = 1/self.input[0]
  temp_sigmoid = np.zeros(SIGMOID)
  temp_output = np.zeros(OUTPUT)
  "GANN input for sigmoid layer"
  for i in range(SIGMOID):
    temp_w = self.gann[0:INPUT, i + INPUT ]
    """print "This are the weights to sigmoid node number ", i
    print temp_w
    print "This are the respective inputs to sigmoid node number ", i
    print self.input"""
    temp_sigmoid[i] = sigmoid(np.sum(np.multiply(temp_w, self.input)))
    #print "This are the temp sigmoid output "
    #print temp_sigmoid
  "GANN input for output layer"
  for i in range(OUTPUT):
    temp_w = self.gann[INPUT:SIGMOID+INPUT, i + SIGMOID + INPUT]
    """print "This are the weights to output node number ", i
    print temp_w
    print "This are the respective inputs to output node number ", i
    print temp_sigmoid"""
    temp_output[i] = sigmoid(np.sum(np.multiply(temp_w, temp_sigmoid)))
  #print temp_output
  (angle, z) = self.vector
  self.vector = ((temp_output[0] - temp_output[1])*2*np.pi, (temp_output[2] - temp_output[3])*DP)
  self.rect = self.new_pos(self.rect, self.vector)

 def new_pos(self, rect, vector):
  "Vector with the direction and how much to move"
  (angle, z) = vector
  #print np.rad2deg(angle)
  (dx,dy) = (z*np.cos(angle), -z*np.sin(angle))
  #print (dx, dy)
  if (rect.centerx>0 and rect.centerx<WIDTH) and (rect.centery>0 and rect.centery<HEIGHT):
    #print "Im a good guy "
    return rect.move(dx,dy)
  else:
    if (rect.centerx < 0):
        #print "-x"
        rect.centerx = WIDTH-1
    elif(rect.centerx > WIDTH):
        #print "++x"
        rect.centerx = 1
    elif(rect.centery < 0):
        #print "-y"
        rect.centery = HEIGHT-1
    elif(rect.centery > HEIGHT):
        #print "++y"
        rect.centery = 1
    return rect.move(dx,dy)

 def draw(self, surface):
  surface.blit(self.image, (self.rect.x, self.rect.y))

 def angle_between(self, object_to):
  dx = float(self.rect.centerx - object_to.rect.centerx)
  dy = float(self.rect.centery - object_to.rect.centery)
  rads = math.atan2(-dy,dx)
  rads = rads % np.pi
  #print rads
  return rads

 def distance_between(self, object_to):
  dx = float(self.rect.centerx - object_to.rect.centerx)
  dy = float(self.rect.centery - object_to.rect.centery)
  z = np.sqrt(np.power(dx,2) + np.power(dy,2))
  return z

 def distance_between_food(self, list_of_food):
  "Reset Input Layer"
  self.input.fill(MAX_DISTANCE)
  for f in list_of_food:
   rads = self.angle_between(f)
   temp_distance = self.distance_between(f)
   if temp_distance < self.input[0]:
     self.input[0] = temp_distance
     self.input[1] = rads

"Screen"
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('GANN')

"Fill background"
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

moscos = []
comidas =[]

for i in range(N_NUMBER_M):
    moscos.append(Mosquitoe((r.randint(0,1), r.randint(0,1)), (r.randint(0,WIDTH-1), r.randint(0,HEIGHT-1)), population[i]))

#comida = Food((619, 459))
posx = r.randint(1,619)
posy =  r.randint(1,459)

comida = Food((posx,posy))
comidas.append(comida)
cambiar = False
"Init clock"
clock = pygame.time.Clock()
t = 0
while True:
 #print str(t)
 t+=1
 if(t==1000):
   terminar(moscos)
   break
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   sys.exit()
  elif event.type == KEYDOWN:
   if event.key == K_ESCAPE:
    sys.exit()

 screen.blit(background, (0, 0))

 for mosco in moscos:
  if cambiar == True:
    posx = r.randint(1,619)
    posy =  r.randint(1,459)
    comida = Food((posx,posy))
    comidas.append(comida)
    cambiar = False

  mosco.distance_between_food(comidas)
  mosco.update()
  mosco.draw(screen)
  comida.draw(screen)

  if mosco.rect.x>=posx and mosco.rect.x <= posx+20:
    if mosco.rect.y>=posy and mosco.rect.y <= posy+20:
      #print "cambiar"
      cambiar = True
      mosco.fitness+=1
      #print str(mosco.fitness)

  if mosco.rect.centerx>=posx and mosco.rect.centerx<= posx+20:
    if mosco.rect.centery>=posy and mosco.rect.centery<= posy+20:
      #print "cambiar"
      cambiar = True
      mosco.fitness+=1
      #print str(mosco.fitness)

 "60 fps"
 clock.tick(CLK)
 pygame.display.update()

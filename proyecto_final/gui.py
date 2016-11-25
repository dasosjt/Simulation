import pygame, math, random, sys
import numpy as np
import random as r
from pygame.locals import *

WIDTH = 640
HEIGHT = 480
MAX_DISTANCE = np.sqrt(np.power(WIDTH, 2) + np.power(HEIGHT, 2))
NODES = 22
INPUT = 2
OUTPUT = 4
SIGMOID = NODES - INPUT - OUTPUT

Generacion = 0
idMayor = 0

INFINITE = float("inf")

DP = 15

N_NUMBER_M = 75
N_NUMBER_C = 15

CLK = 1000

T = 1000

mean = 0

population = np.random.randint(-100,100,(N_NUMBER_M, NODES*NODES))
population = np.multiply(population, 0.01)

def terminar(moscos):
  mayor = 0
  for mosco in moscos:
    #print "El fitness del mosco " + str(moscos.index(mosco)) + " es de " + str(mosco.fitness)
    if mosco.fitness > mayor:
      mayor = mosco.fitness
      idMayor = moscos.index(mosco)
  #print "El fitness mayor es " + str(mayor) + " del mosco " + str(idMayor)

def nuevaPoblacion(moscos):
  mayor = 0
  mean = 0
  for mosco in moscos:
    mean += mosco.fitness
    if mosco.fitness > mayor:
      mayor = mosco.fitness
  mean = mean/100.

  buenosMoscos = []
  for mosco in moscos:
    if mosco.fitness > mean:
      buenosMoscos.append(mosco)
  l = len(buenosMoscos)

  print "Media " + str(mean)
  print "L " + str(l)

  moscos = []

  for i in range(N_NUMBER_M):
    a = r.randint(0,len(buenosMoscos)-1)
    temp_mosco = buenosMoscos[a]

    p_mutacion = 0.3
    p_crossover = 0.5
    p_random = 0.05

    new_gann = np.random.randint(-100,100,(1, NODES*NODES))
    new_gann = np.multiply(new_gann, 0.01)
    RGB = (20, 255, 20)
    if(p_random < r.uniform(0,1)):
     if(p_crossover < r.uniform(0,1)):
      a = r.randint(0,len(buenosMoscos)-1)
      temp_mosco2 = buenosMoscos[a]
      a = r.randint(0,len(buenosMoscos)-1)
      temp_mosco3 = buenosMoscos[a]
      if(p_mutacion < r.uniform(0,1)):
        #print "MUTACION"
        new_gann = np.zeros((NODES,NODES))
        for i in range(INPUT-1):
         for j in range(INPUT-1):
          if(r.randint(0,1)==1):
             new_gann[i,j] = temp_mosco.gann[i,j] - r.uniform(0, 0.5)
          else:
             new_gann[i,j] = temp_mosco.gann[i,j] + r.uniform(0, 0.5)
        for i in range(SIGMOID-1):
         for j in range(SIGMOID-1):
          if(r.randint(0,2)==1):
             new_gann[INPUT+i,INPUT+j] = temp_mosco2.gann[INPUT+i,INPUT+j] -r.uniform(0, 0.15)
          elif(r.randint(0,2)==1):
             new_gann[INPUT+i,INPUT+j] = temp_mosco2.gann[INPUT+i,INPUT+j] + r.uniform(0, 0.15)
          else:
             new_gann[INPUT+i,INPUT+j] = temp_mosco2.gann[INPUT+i,INPUT+j]
        for i in range(OUTPUT-1):
         for j in range(OUTPUT-1):
          new_gann[INPUT+SIGMOID+i,INPUT+SIGMOID+j] = temp_mosco3.gann[INPUT+SIGMOID+i,INPUT+SIGMOID+j]
        new_gann = new_gann.reshape((1, NODES*NODES))
      else:
        #print "CROSS_OVER"
        new_gann = np.zeros((NODES,NODES))
        for i in range(INPUT-1):
         for j in range(INPUT-1):
          new_gann[i,j] = temp_mosco.gann[i,j]
        for i in range(SIGMOID-1):
         for j in range(SIGMOID-1):
          new_gann[INPUT+i,INPUT+j] = temp_mosco2.gann[INPUT+i,INPUT+j]
        for i in range(OUTPUT-1):
         for j in range(OUTPUT-1):
          new_gann[INPUT+SIGMOID+i,INPUT+SIGMOID+j] = temp_mosco3.gann[INPUT+SIGMOID+i,INPUT+SIGMOID+j]
        new_gann = new_gann.reshape((1, NODES*NODES))
     else:
      "BEST"
      RGB = (0, 0, 0)
      new_gann = temp_mosco.gann
    moscos.append(Mosquitoe((r.randint(0,1), r.randint(0,1)), (r.randint(0,WIDTH-1), r.randint(0,HEIGHT-1)), new_gann, RGB))
  return moscos,mean,l

def sigmoid(number):
  result = 1/(1 + np.exp(-number))
  return result

class Food(pygame.sprite.Sprite):
 "Returns: Food object"
 "Function: draw"

 def __init__(self, position):
  pygame.sprite.Sprite.__init__(self)
  self.image = pygame.Surface([10, 10])
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

 def __init__(self, vector, position, gann, RGB):
  pygame.sprite.Sprite.__init__(self)
  self.image = pygame.Surface((10, 10))
  self.image = self.image.convert()
  self.RGB = RGB
  self.image.fill(self.RGB)
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
  if(self.input[0] == 0):
      self.input[0] = INFINITE
  else:
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
  try:
    self.rect = self.new_pos(self.rect, self.vector)
  except:
    self.rect = self.rect.move(0,0)

 def new_pos(self, rect, vector):
  "Vector with the direction and how much to move"
  (angle, z) = vector
  #print np.rad2deg(angle)
  (dx, dy) = (z*np.cos(angle), -z*np.sin(angle))
  #print (dx, dy)
  if not((rect.centerx>0 and rect.centerx<WIDTH) and (rect.centery>0 and rect.centery<HEIGHT)):
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
  return rect.move(dx, dy)

 def draw(self, surface):
  #surface.blit(self.image, (self.rect.x, self.rect.y))
  if(3*self.fitness < 30):
      pygame.draw.circle(surface, self.RGB, (self.rect.x, self.rect.y), 3*self.fitness)
  else:
      pygame.draw.circle(surface, self.RGB, (self.rect.x, self.rect.y), 30)

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

 def reset_fitness(self):
  self.fitness = 0

 def reset_pos(self):
  self.rect.x = r.randint(0,WIDTH-1)
  self.rect.y = r.randint(0,HEIGHT-1)

Generacion = 0
l = 0
while Generacion < 200:

 "Screen"
 pygame.init()
 screen = pygame.display.set_mode((WIDTH, HEIGHT))
 pygame.display.set_caption('GANN')

 "Fill background"
 background = pygame.Surface(screen.get_size())
 background = background.convert()
 background.fill((255, 255, 255))

 if Generacion == 0:
  moscos = []
  comidas = []
  for i in range(N_NUMBER_M):
     moscos.append(Mosquitoe((r.randint(0,1), r.randint(0,1)), (r.randint(0,WIDTH-1), r.randint(0,HEIGHT-1)), population[i], (20, 255, 20)))

  for i in range(N_NUMBER_C):
     comidas.append(Food((r.randint(1,WIDTH-1), r.randint(1,HEIGHT-1))))

 else:
  mean=0
  moscos,mean,l = nuevaPoblacion(moscos)
  comidas = []

  for i in range(N_NUMBER_C):
     comidas.append(Food((r.randint(1,WIDTH-1), r.randint(1,HEIGHT-1))))


 "Init clock"
 clock = pygame.time.Clock()
 t = 1
 while True:
  if(t==T):
    Generacion += 1
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
   mosco.distance_between_food(comidas)
   mosco.update()
   mosco.draw(screen)

   for comida in comidas:
    if(pygame.sprite.collide_rect(mosco, comida)):
     comida.rect.x = r.randint(1,WIDTH-1)
     comida.rect.y = r.randint(1,HEIGHT-1)
     mosco.fitness+=1
    comida.draw(screen)

  myfont = pygame.font.SysFont("calibri", 25)
  label = myfont.render("GENERATION : "+str(Generacion+1), 24, (0,0,0))
  label2 = myfont.render("t : "+str(t), 24, (0,0,0))
  label3 = myfont.render("Mean of food eaten by each Mosquitoe: "+str(mean), 24, (0,0,0))
  label4 = myfont.render("Length of Mosquitoes that ate over the mean : "+str(l), 24, (0,0,0))
  screen.blit(label, (WIDTH/2 - 75, 40))
  screen.blit(label2, (10, HEIGHT-80))
  screen.blit(label3, (10, HEIGHT-60))
  screen.blit(label4, (10, HEIGHT-40))

  "60 fps"
  clock.tick(CLK)
  pygame.display.update()
  t += 1

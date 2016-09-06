# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 20:00:07 2016

@author: Diego Sosa
"""

import numpy as np
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def f1(p):
    pn = Point(p.x*0.85 + p.y*0.04, p.x*-0.04 + p.y*0.85 + 1.6)
    return pn
def f2(p):
    pn = Point(p.x*(-0.15)+0.28*p.y, p.x*0.26 + p.y*0.24 + 0.44 )
    return pn
def f3(p):
    pn = Point(p.x*0.2+p.y*(-0.26), p.x*0.23+p.y*0.22+1.6)
    return pn
def f4(p):
    pn = Point(0, p.y*0.16)
    return pn
    
pn = Point(1.0,1.0)
c = 1000000
listPointsX = []
listPointsY = []
#genero una gran lista de numeros psealeatorios
values = np.random.random(c)

for i in values:
    #otorgo la probabilidad a cada función
    if i < 0.85:
        #print 'f1'
        pn = f1(pn)
    elif 0.85 < i and i < 0.92:
        #print 'f2'
        pn = f2(pn)
    elif 0.92 < i and i < 0.99:
        #print 'f3'
        pn = f3(pn)
    elif 0.99 < i:
        #print 'f3'
        pn = f4(pn)
    #print i
    #agrego las coordenadas para plotear
    listPointsX.append(pn.x)
    listPointsY.append(pn.y)

#print listPointsX
#print listPointsY

plt.plot(listPointsX, listPointsY, 'ro', ms = 0.5, alpha = 0.5)
plt.show()
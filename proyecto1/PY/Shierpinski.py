# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 18:32:25 2016

@author: Diego Sosa
"""

import numpy as np
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def f1(p):
    pn = Point(p.x/2, p.y/2)
    return pn
def f2(p):
    pn = Point(p.x/2+0.5, p.y/2)
    return pn
def f3(p):
    pn = Point(p.x/2+0.25, p.y/2+0.5)
    return pn
    
pn = Point(1.0,1.0)
c = 100000
listPointsX = []
listPointsY = []
#genero una gran lista de numeros según c
values = np.random.random(c)

for i in values:
    #otorgo la probabilidad a cada funcion
    if i < 0.333:
        #print 'f1'
        pn = f1(pn)
    elif 0.333 < i and i < 0.666:
        #print 'f2'
        pn = f2(pn)
    elif 0.666 < i and i < 1:
        #print 'f3'
        pn = f3(pn)
    #print i
    listPointsX.append(pn.x)
    listPointsY.append(pn.y)

#print listPointsX
#print listPointsY

#ploteo los puntos
plt.plot(listPointsX, listPointsY, 'ro', ms =0.5, alpha=0.3)
plt.show();

    
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 11:32:36 2016

@author: Diego Sosa
"""

import math
import random


def e(lam):
    return -(1/lam)*math.log(random.random(),math.exp(1))
    
def normal(M,sigma):
    while True:
        y1 = e(1)
        y2 = e(1)
        if (y2 - (y1-1)**2)/2 > 0:
            y = (y2 - (y1-1)**2)/2
            u = random.random()
            if u <= 0.5:
                return M + sigma*y1
            else:
                return M - sigma*y1
    
def uniform(a,b):
    x = random.random()
    r = (b-a)*x+a
    return r  
    
def valuePN(V,t):
    r = V[0]
    for i in range(1,len(V)):
        r += V[i]/((1+t)**i)
    return r

print "Ejercicio 3"
print "Simulación con 100 corridas"
t = 0.1
iteraciones = 100
p_hotel,p_cc = 0,0
for i in range(iteraciones):
    hotel = [-800, normal(-800,50), normal(-800,100), normal(-700,150), normal(300,200), normal(400,200), normal(500,200), uniform(200,8440)]
    cc = [-900, normal(-600,50), normal(-200,50), normal(-600,100), normal(250,150), normal(350,150), normal(400,150), uniform(1600,6000)]
    p_hotel += valuePN(hotel,t)
    p_cc += valuePN(cc,t)
print "Promedio de VPN en la inversión del proyecto del Hotel: " + str(p_hotel/iteraciones)
print "Promedio de VPN en la inversión del proyecto del Centro Comercial: " + str(p_cc/iteraciones)
if p_hotel > p_cc:
    print "El proyecto mas rentable es el Centro Comercial."
else:
    print "El proyecto mas rentable es el Hotel."

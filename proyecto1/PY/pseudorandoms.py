# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 20:34:29 2016

@author: Diego Sosa
"""

import random


def g1(x):
    return (pow(5,5)*x % (pow(2,35)-1))
    
def g2(x):
    return (pow(7,5)*x % (pow(2,31)-1))

def g3(x):
    return random.random()
    
N = 100000
xi1 = 0.5

def appG(g, N, xi1):
    l = [0]*10 #inicializo lista
    print g
    for i in range(N):
        #uso el generador dependiente
        if g == "g1":            
            xi = g1(xi1)/(pow(2,35)-1)
            xi1 = g1(xi1)
        elif g == "g2":            
            xi = g2(xi1)/(pow(2,31)-1)
            xi1 = g2(xi1)
        elif g == "g3":
            xi = g3(xi1)
        #evaluo los aciertos
        if xi < 0.1:
            l[0] += 1
        elif 0.1 < xi and xi < 0.2:
            l[1] += 1
        elif 0.2 < xi and xi < 0.3:
            l[2] += 1
        elif 0.3 < xi and xi < 0.4:
            l[3] += 1
        elif 0.4 < xi and xi < 0.5:
            l[4] += 1
        elif 0.5 < xi and xi < 0.6:
            l[5] += 1
        elif 0.6 < xi and xi < 0.7:
            l[6] += 1
        elif 0.7 < xi and xi < 0.8:
            l[7] += 1
        elif 0.8 < xi and xi < 0.9:
            l[8] += 1
        elif 0.9 < xi and xi < 1.0:
            l[9] += 1
    #imprimo los resultados
    for j in range(len(l)):
        percent = float(l[j])/N*100
        aster = "*" * int(percent)
        print str(float(j)/10) +" - " + str(float(j+1)/10)+": "+ aster + " ("+str(l[j])+", %"+ str(percent)+")"
        
print "\n \n 100 Iteraciones"        
appG("g1", 100, xi1)
appG("g2", 100, xi1)
appG("g3", 100, xi1)

print "\n \n 500 Iteraciones"
appG("g1", 5000, xi1)
appG("g2", 5000, xi1)
appG("g3", 5000, xi1)

print "\n \n 100000 Iteraciones"
appG("g1", N, xi1)
appG("g2", N, xi1)
appG("g3", N, xi1)    




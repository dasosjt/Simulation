# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 12:18:17 2016

@author: Diego Sosa
"""

import random 

def varPeriodico(n, nf, it):
    total = -(1.5*n*it)
    for i in range(0,it):
        x = random.random()
        if x < 0.3:
            total += 2.5*n
        elif (0.3 < x and x < 0.7):
            total += 2.5*n
            total += 0.5*(nf-n)
        else:
            total += 2.5*n
            total += 0.5*(nf-n)
    return total
        
print "Ejercicio 4"
print "1 MES"
n = 9
print "Ganancia con 9 periodicos: "  +str(varPeriodico(n,11,30))
n = 10
print "Ganancia con 10 periodicos: "  +str(varPeriodico(n,11,30))
n = 11
print "Ganancia con 11 periodicos: "  +str(varPeriodico(n,11,30))
print "1 AÑO"
n = 9
print "Ganancia con 9 periodicos: "  +str(varPeriodico(n,11,365))
n = 10
print "Ganancia con 10 periodicos: "  +str(varPeriodico(n,11,365))
n = 11
print "Ganancia con 11 periodicos: "  +str(varPeriodico(n,11,365))
print "10 AÑOS"
n = 9
print "Ganancia con 9 periodicos: "  +str(varPeriodico(n,11,3650))
n = 10
print "Ganancia con 10 periodicos: "  +str(varPeriodico(n,11,3650))
n = 11
print "Ganancia con 11 periodicos: "  +str(varPeriodico(n,11,3650))
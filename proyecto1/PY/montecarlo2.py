# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 11:52:16 2016

@author: Diego Sosa
"""

import numpy as np
#inicializo valores
N = 1000000
#genero lista random
x = np.random.random(N)
y = np.random.random(N)

u = ((1/x)-1)
#evalue integral en el vector, mantengo todos los valores en el vector sin sumar
integral = (1.0/N) * (u*np.exp(-(u+u*y)))/(x**2)
#sumo todos los valores de la integral
integralR = sum(integral)
    
print integralR

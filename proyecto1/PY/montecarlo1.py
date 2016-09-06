# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 23:51:50 2016


@author: Diego Sosa
"""

import numpy as np
#inicializo valores
x=0
integral = 0
N = 100
#genero lista random
x = np.random.random(N)
xm2 = -pow(x,2)
x2 = pow(x,2)
#evalue integral en el vector, mantengo todos los valores en el vector sin sumar
integral = (2.0/N)*(np.exp(xm2)+(np.exp(-1/x2))/x2)
#sumo todos los valores de la integral
integralR = sum(integral)
    
print integralR
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 04 14:19:52 2016

@author: Diego Sosa
"""

import matplotlib.pyplot as plt
import numpy as np

def p1(x):
    return x*np.exp(x)

def p2(x):
    return 2*x*np.exp(x)

def acump(pi, npi):
    if(sum(npi) != 1):
        print "Suma de "
        
    return 0


#gaussian_numbers = np.random.randn(100)
#plt.hist(gaussian_numbers)


pi = [p1, p2]
npi = [0.5, 0.5]

uniform_rands = np.random.random(1000000)

param = 1.8
transformed_rands = [1 / param * np.log(1 / (1 - x)) for x in uniform_rands]
plt.hist(transformed_rands, bins=500, normed=True)

plt.show()
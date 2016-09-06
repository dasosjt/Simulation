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
    return -2*x*np.exp(x)

def v(f, dist):
    if(sum(dist) != 1):
        print "Suma de probabilidades no es 1"
    else: 
        print "Suma de probabilidades es 1"
        interval = []
        for u in dist:
            if len(interval) != 0:
                interval.append(u+interval[-1])
            else:
                interval.append(u)
        print interval
        x = np.random.random(1000)
        c = [0]*len(interval)
        for xn in x:
            for i in range(0,len(interval)):
                if xn < interval[i] and xn > interval[i-1]:
                    print "C "+str(i)+" +1 con el valor "+ str(xn)
                    c[i]+=1
                if i == 0 and xn < interval[0]:
                    print "C "+str(i)+" +1 con el valor "+ str(xn)
                    c[i]+=1
        print c[0]
        print c[1]
        print c[2]
        print c[3]
        return c
            
f = [p1, p2]
dist = [0.1, 0.3, 0.2, 0.4]
plt.hist(v(f,dist), 500, normed=100, facecolor='g', alpha=0.75)
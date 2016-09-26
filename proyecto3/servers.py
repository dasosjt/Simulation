import math as mt
from random import random

def exponencial(lambdaP):
    u=random()
    x=-(1.0/lambdaP)*mt.log(u)
    return x

def findIndexOf(td, value):
    try:
        idx = td.index(value)
    except Exception:
        return -1
    return idx

t = 0
n = 0
Na = 0
Nd = 0
C = []
A = []
D = []
T = 2500
servers = 29
lambdapp = 40
a = 10

inf = float('inf')

ta = exponencial(lambdapp)
td = [inf]*servers
ss = [0]*servers
C = [0]*servers
tx = [0]*servers


while t < T or n >= 0:
    print t
    #print "A, ",A
    #print "D, ",D
    #print "C, ",C
    if ta == min(ta, min(td)) and ta < T:
        print "Case 1"
        t = ta
        Na += 1
        n += 1
        ta = t + exponencial(lambdapp)
        A.append(t)
        tempindex = findIndexOf(td, inf)
        if tempindex != -1:
            Y = exponencial(a)
            td[tempindex] = t + Y
            ss[tempindex] = Na
            tx[tempindex] += Y
            C[tempindex] += 1

    elif min(td) < ta and min(td) < T:
        print "Case 2"
        t = min(td)
        Nd += 1
        n += -1
        D.append(t)
        tempindex = findIndexOf(td, t)
        if n <= len(td):
            td[tempindex] = inf
            ss[tempindex] = 0
        else:
            Na += 1
            A.append(t)
            Y = exponencial(a)
            td[tempindex] = t + Y
            ss[tempindex] = Na
            tx[tempindex] += Y
            C[tempindex] += 1

    elif min(ta, min(td)) > T and n > 0:
        print "Case 3"
        t = min(td)
        n += -1
        Nd += 1
        D.append(t)
        tempindex = findIndexOf(td, t)
        if n > 0:
            Na += 1
            A.append(t)
            Y = exponencial(a)
            td[tempindex] = t + Y
            ss[tempindex] = Na
            tx[tempindex] += Y
            C[tempindex] += 1

    elif n == 0:
        print "Case 4"
        break
print sum(C)
print C
print sum(tx)
print tx
print n

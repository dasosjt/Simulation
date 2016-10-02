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
servers = 10
lambdapp = 40
a = 10

inf = float('inf')

ta = exponencial(lambdapp)
td = [inf]*servers
ss = [0]*servers
C = [0]*servers
tx = [0]*servers
cola = []


while t < T or n >= 0:
    print C
    if ta == min(ta, min(td)) and ta < T:
        print "Case 1"
        t = ta
        Na += 1
        ta = t + exponencial(lambdapp)
        t = ta
        A.append(t)
        if n  > len(td)-1:
            n += 1
            en_cola = exponencial(lambdapp)
            cola.append(en_cola)
        else:
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
        if n <= len(td)-1:
            if n == 1:
                n = 0
            else:
                n = n - 1
            td[tempindex] = inf
            ss[tempindex] = 0
        else:
            n += 1
            A.append(t)
            Y = exponencial(a)
            td[tempindex] = t + Y
            ss[tempindex] = Na
            tx[tempindex] += Y
            C[tempindex] += 1

    elif min(ta, min(td)) > T and n > 0:
        t = min(td)
        n += -1
        Nd += 1
        D.append(t)
        tempindex = findIndexOf(td, t)
        if n > 0:
            Nd += 1
            Y = exponencial(a)
            td[tempindex] = t + Y
            ss[tempindex] = Na
            tx[tempindex] += Y
            C[tempindex] += 1

    elif n == 0:
        #print "Case 4"
        break
if len(cola) > 0:
    pcola = sum(cola)/len(cola)
else:
    pcola = sum(cola)

if sum(cola) > 0:
    scola = len(cola)/sum(cola)
else:
    scola = len(cola)


nQ = 0
tQ = 0

for i in range(0, len(tx)-1):
    if(0 < D[i]-A[i+1]):
        nQ += 1
        tQ += (D[i]-A[i+1])
tQ = sum(tx) - tQ

print "En promedio cada servidor atendio ", sum(C)/servers

for c0 in C:
    print "El servidor atendio ", c0

print "Los servidores estuvieron ocupados", sum(tx)

for tx0 in tx:
    print "El servidor estuvo ocupado ", tx0

print "Los servidores estuvieron desocupados", sum(tx) - T

for tx0 in tx:
    print "El servidor estuvo desocupado ", T - tx0

print "Cantidad de solicitudes que estuvieron en cola ",nQ

print "En promedio cada solicitud estuvo en cola ", tQ/(nQ*servers*a)

print "En promedio cada segundo estuvo en cola ", tQ/(T*servers*a)

print "Ultima salida ocurrio", t

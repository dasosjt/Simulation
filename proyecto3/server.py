import math as mt
import random as rand

Tp = 0
t = 0
Na = 0
Nd = 0
n = 0
servidores = 1

inf = float("inf")

T = 5

A = [0]*T #tiempo de llegada de la i-esima solicitud
D = [0]*T #tiempo de salida de la i-esima solicitud
ta = mt.exp(rand.random()) #llegada del primer cliente
td = inf #salida del cliente


while t <= T:
    print "t = ", t
    print "n = ", n
    print "ta = ", ta
    print "td = ", td
    print A
    print D
    if ta <= td and ta <= T:
        print " Case 1, llego un solicitud al sistema"
        print "     ta =  ", ta
        print "     td =  ", td
        t = ta
        Na = Na + 1
        n = n + 1
        A[Na-1] = ta
        ta = t + mt.exp(rand.random())
        if n == 1:
            td = t + mt.exp(rand.random())

    elif td < ta and td <= T:
        print " Case 2, tenemos una salida del sistema"
        print "     ta =  ", ta
        print "     td =  ", td
        t = td
        n = n - 1
        Nd = Nd + 1
        D[Nd-1] = td
        if n == 0:
            td = inf
        else:
            td = t + mt.exp(rand.random())


    elif min(ta, td) > T and n > 0:
        print " Case 3"
        print "     ta =  ", ta
        print "     td =  ", td
        t = td
        n = n - 1
        Nd = Nd + 1
        D[Nd-1] = td
        if n > 0:
            td = t + mt.exp(rand.random())

    elif min(ta, td) > T and n == 0:
        print " Case 4"
        print "     ta =  ", ta
        print "     td =  ", td
        Tp = max(t - T, 0)
        break

Sp = []
iddleT = []
Ld = 0
for i in range(len(A)-1):
    if D[i] - A[i] != 0:
        Sp.append(D[i] - A[i])

for i in range(len(A)-1):
    if i < len(A)-2:
        if(A[i+1]-D[i] > 0):
            iddleT.append(A[i+1]-D[i])
while i in range(len(D)-1):
    print D[-i]
    if D[-i] > 1:
        print ""
        Ld = D[-i]
        break
    i = i +1

print "Cada servirdor atendio esta cantidad de solicitudes: ", Nd/servidores
print "Cada servidor estuvo ocupado: ", sum(Sp)
print "Cada servidor estuvo iddle: ", sum(iddleT)
print "En cola quedaron: ", n
print "La ultima salida del sistema fue: ", Ld
print A
print D

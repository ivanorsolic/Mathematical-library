# -*- coding: utf-8 -*-
import numpy as np

def nema():
    print("Nema presjeka!")
    quit()

def ispis(i, j, k):
    print("Koordinata i je %f.\nKoordinata j je %f.\nKoordinata k je %f." % (i,j,k))

def vektor():
    v = np.empty(3)
    for i in range(3):
        v[i] = raw_input('Unesite %d. koordinatu: ' % (i+1))
    return v

def normalizacija(vektor):
    djelitelj = np.sqrt((np.square(vektor[0])) + (np.square(vektor[1])) + (np.square(vektor[2])))
    vektor[0] = vektor[0]/djelitelj
    vektor[1] = vektor[1]/djelitelj
    vektor[2] = vektor[2]/djelitelj
    return vektor

print("Unesite koordinate početne točke zrake (p):\n")
p=vektor()

ispis(p[0], p[1], p[2])

print("Unesite vektor smjera: \n")
u=normalizacija(vektor())

ispis(u[0],u[1],u[2])

print("Unesite koordinate normale ravnine (n):\n")
n=vektor()

ispis(n[0], n[1], n[2])

d = float(raw_input("Unesite skalar d: "))

c=np.dot(u,n)
if c == 0:
    nema()

alfa = np.divide((np.subtract(d,np.dot(p,n))),c)
if alfa < 0:
    nema()

q = np.empty(3)
q=np.add(p,np.dot(alfa,u))

ispis(q[0], q[1], q[2])

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

#Početna točka unos i ispis
print("Unesite koordinate početne točke zrake (p):\n")
p=vektor()
ispis(p[0],p[1],p[2])

#Vektor smjera unos, normalizacija i ispis
print("Unesite vektor smjera: \n")
u=normalizacija(vektor())

ispis(u[0],u[1],u[2])

print("Unesite prvi vrh trokuta:\n")
v0=vektor()
ispis(v0[0],v0[1],v0[2])

print("Unesite drugi vrh trokuta:\n")
v1=vektor()
ispis(v1[0],v1[1],v1[2])

print("Unesite treći vrh trokuta:\n")
v2=vektor()
ispis(v2[0],v2[1],v2[2])

#prekomputacija n, d, ubeta, ugamma

e1 = np.subtract(v1,v0)
e2 = np.subtract(v2,v0)
n = np.cross(e1,e2)
d = np.dot(n, v0)
a = np.dot(e1, e1)
b = np.dot(e1,e2)
c = np.dot(e2,e2)
D = np.subtract(np.dot(a,c),np.square(b))
A = np.divide(a, D)
B = np.divide(b, D)
C = np.divide(c, D)
ubeta = np.subtract(np.dot(C,e1),np.dot(B,e2))
ugamma = np.subtract(np.dot(A,e2),np.dot(B,e1))

#Glavni algoritam
#Ray-Plane intersection algoritam za dobijanje q
cRP = np.dot(u, n)
alfa1 = np.divide(np.subtract(d, np.dot(p,n)),cRP)
q = np.empty(3)
q=np.add(p,np.dot(alfa1,u))
r = np.subtract(q,v0)
beta = np.dot(ubeta,r)
gamma = np.dot(ugamma,r)
alfa = 1 - beta - gamma
print("Baricentričke koordinate su: ")
ispis(alfa, beta, gamma)

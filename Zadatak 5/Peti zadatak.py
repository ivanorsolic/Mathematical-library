# -*- coding: utf-8 -*-
import numpy as np

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

def nema():
    print("Nema presjeka!")
    quit()

print("Unesite koordinate početne točke zrake (p):\n")
p=vektor()

ispis(p[0], p[1], p[2])

print("Unesite vektor smjera: \n")
u=normalizacija(vektor())

ispis(u[0], u[1], u[2])

print("Unesite koordinate središta sfere (c):\n")
c=vektor()

ispis(c[0], c[1], c[2])

polumjer=-1
while polumjer<0:
    polumjer = float(raw_input("Unesite polumjer (r>0!): "))

# c - središte sfere
# p - početna točka zrake
# u - jedinični vektor
# polumjer ==
q=np.empty(3)
alfa = np.dot(np.subtract(c,p),u)
q=np.add(p,np.dot(alfa,u))

bSq = np.linalg.norm(np.subtract(q,c))
if bSq > np.square(polumjer):
    nema()

a = np.sqrt(np.square(polumjer)-bSq)
if alfa>=a:
    tocka1=np.empty(3)
    tocka1=np.subtract(q,np.dot(a,u))
    ispis(tocka1[0], tocka1[1], tocka1[2])
if np.add(alfa,a)>0:
    tocka2=np.empty(3)
    tocka2=np.add(q,np.dot(a,u))
    ispis(tocka2[0], tocka2[1], tocka2[2])
else:
    nema()

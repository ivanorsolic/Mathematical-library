# -*- coding: utf-8 -*-
import numpy as np

def ispis(i, j, k):
    print("Koordinata i je %f.\nKoordinata j je %f.\nKoordinata k je %f." % (i,j,k))

def vektor():
    v = np.empty(3)
    for i in range(3):
        v[i] = input('Unesite %d. koordinatu: ' % (i+1))
    return v

def nema():
    print("Nema presjeka!")
    quit()

def normalizacija(vektor):
    djelitelj = np.sqrt((np.square(vektor[0])) + (np.square(vektor[1])) + (np.square(vektor[2])))
    vektor[0] = vektor[0]/djelitelj
    vektor[1] = vektor[1]/djelitelj
    vektor[2] = vektor[2]/djelitelj
    return vektor

def ravnine(broj):
    ravnine = {key: None for key in range(broj)}
    for key in ravnine:

        ravnina = key+1
        skalar = float(raw_input("Unesite skalar ravnine %d:" % (ravnina)))

        print("Normala ravnine:")
        normala = vektor()

        ravnine[key] = [skalar, normala]

    return ravnine

print("Unesite koordinate početne točke zrake (p):\n")
p = vektor()

print("Unesite vektor smjera: \n")
u=normalizacija(vektor())

k = int(raw_input('Unesite broj ravnina koje definiraju politop: '))
ravnine = ravnine(k)
fMax = -np.inf
bMin = np.inf

for i in range(k):
    #Ray to plane intersection
    k -= 1
    skalar = ravnine[k][0]
    normala = ravnine[k][1]

    s = np.dot(u, normala)
    if s==0:    #Paralelno sa ravninom?
        if np.dot(p, normala)>skalar:
            nema()

    alfa = np.subtract(skalar,np.dot(p,normala))
    if np.dot(u,normala) < 0:   #Ispred presjeka?
        if alfa > fMax:
            if alfa > bMin:
                nema()
            fMax = alfa

    else: #else, back intersection
        if alfa < bMin:
            if (alfa < 0) or (alfa < fMax):
                nema()
                bMin = alfa

if fMax > 0:
    alfa = fMax
else:
    alfa = bMin

q = np.add(p, np.dot(alfa, u))
print(q)

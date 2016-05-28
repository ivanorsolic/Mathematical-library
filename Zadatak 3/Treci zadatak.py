# -*- coding: utf-8 -*-
import numpy as np
#http://www.starkeffects.com/snells-law-vector.shtml

def ispis(i, j, k):
    print("Koordinata i je %f.\nKoordinata j je %f.\nKoordinata k je %f." % (i,j,k))

def vektor():
    v = np.empty(3)
    for i in range(3):
        v[i] = input('Unesite %d. koordinatu: ' % (i+1))
    return v

def normalizacija(vektor):
    djelitelj = np.sqrt((np.square(vektor[0])) + (np.square(vektor[1])) + (np.square(vektor[2])))
    vektor[0] = vektor[0]/djelitelj
    vektor[1] = vektor[1]/djelitelj
    vektor[2] = vektor[2]/djelitelj
    return vektor

print("Unesite koordinate vektora normale:\n")
n=vektor()

ispis(n[0], n[1], n[2])

print("Unesite koordinate vektora v:\n")
v = normalizacija(vektor())
ispis(v[0], v[1], v[2])

indeks = input("Unesite indeks loma: ")
negn = np.empty(3)
negn = [x * (-1) for x in n]
negprodukt = np.cross(negn,v)
produkt = np.cross(n,v)
skalar_produkt = np.vdot(produkt, produkt)
p_korijen = 1-((indeks*indeks) * skalar_produkt)
korijen = np.sqrt(p_korijen)
n_puta_produkt = np.cross(n, negprodukt)
#kvad_produkt = [x * x for x in produkt]

prvi = [x * indeks for x in n_puta_produkt]
drugi = [x * korijen for x in n]

rezultat = np.empty(3)
rezultat[0] = prvi[0] - drugi[0]
rezultat[1] = prvi[1] - drugi[1]
rezultat[2] = prvi[2] - drugi[2]

print("Rezultat:")
ispis(rezultat[0], rezultat[1], rezultat[2])

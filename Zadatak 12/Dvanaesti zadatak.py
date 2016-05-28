f (x, y, z) = Ax2 + By2 + Cz2 + Dxy + Exz + Fyz + Gx + Hy + Jz + K.
p(α) = p + αu
p(α) = (i, j, k) + (αi1, αj1, αk1)
p(α) = (i + αi1)

za α ≥ 0:
  f (p(α)) = 0
  f (p(α)) = aα2 + bα + c.

p = početna točka
u = jedinični vektor smjera

p + αu = vektor (i, j, k)

f(i, j, k) = iα^2 + bα + c

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

print("Unesite koordinate početne točke zrake (p):\n")
p = vektor()

print("Unesite vektor smjera: \n")
u = normalizacija(vektor())

palfa = np.add(p, np.dot(alfa, u))

import copy
liste2 = []
zahl = []
tab = {}

def input1():
    d = ""
    ein = input(">>> ")
    ein = ein.replace(" ", ";")
    liste = ein.split(";")
    liste_c = copy.copy(liste)
    for i in range(0,len(liste_c)):
        if liste_c[i] in liste2:
            liste.remove(liste[i])

    for i in liste:
        liste2.append(i)

    for i in range(len(liste_c)):
        g = " " + str(liste2.index(liste_c[i]))
        d += g
    l = len(tab) + 1
    tab[l] = d

    liste.clear()
    liste_c.clear()

input1()
input1()
input1()
print(liste2)
print(tab)
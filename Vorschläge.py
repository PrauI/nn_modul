import copy
liste = []
liste2 = []
zahl = []
tab = {}

def main():
    print(tab)
    print(liste2)
    print(zahl)

def Zahl():
    global liste, zahl
    for i in range(0,len(liste)):
        zahl.append(len(zahl)+2)
    tabelle()

def tabelle():
    global tab, ein1
    gr = str(0)
    for i in range(0,len(liste)):
        platz = liste2.index(liste[i])
        gr += str(zahl[platz])
    g = len(tab) + 1
    tab[g] = gr
    liste.clear()
    if ein1 == "stop_all":
        main()
    else:
        eingabe()

# wörter eingeben
def eingabe():
    global liste, liste2, ein1
    ein = input()
    ein1 = copy.deepcopy(ein)
    ein = ein.replace(" ",";")
    liste = ein.split(";")
    for i in range(0,len(liste)):
        if liste[i] in liste2:
            liste.remove(liste[i])
        liste2.append(liste[i])
    Zahl()

eingabe()

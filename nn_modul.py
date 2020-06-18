y2 = [1,1,1,0]
w2 = [-1,0,0]
x = [[1,0,0], [1,1,0], [1,0,1], [1,1,1]]

y_hat = []
def dot(daten,weights):
    ergebnis = []
    for i in daten:
        d = 0
        for a in range(len(i)):
            d += i[a] * weights[a]
        ergebnis.append(d)
    return ergebnis

def aktivierung_heaviside(ergebnis):
    loesung_hat = []
    for i in ergebnis:
        if i > 0:
            loesung_hat.append(1)
        else:
            loesung_hat.append(0)
    return loesung_hat

def lernen(daten, loesung, weights, iterations):
    for i in range(iterations):
        error = []
        for i in range(len(loesung)):
            error.append(loesung[i] - aktivierung_heaviside(dot(daten, weights))[i])
        print("Fehler:", error)
        for i in range(len(error)):
            if not error[i] == 0:
                for e in range(0,len(daten[i])):
                    weights[e] = weights[e] + error[e]
    return aktivierung_heaviside(dot(daten, weights))

print("ergebnis:",lernen(x, y2, w2, 500))

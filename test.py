import nn_modul
x = [[1,0,0], [1,1,0], [1,0,1], [1,1,1]]
y1 = [0,1,1,1]
y2 = [1,1,1,0]
w1 = [-1,1,1]
w2 = [1,1,-1]

#print(nn_modul.dot(x, w))

er_y1 = nn_modul.lernen(x, y1, w1, 500)
er_y2 = nn_modul.lernen(x, y2, w2, 500)
print(w1)
print(w2)
print()

print(er_y1, er_y2)

ergebnis_ = []
for i in range(len(er_y1)):
    vorrueber = [1,er_y1[i] ,er_y2[i]]
    ergebnis_.append(vorrueber)
    vorrueber = []

print(ergebnis_)
y_ = [0, 1, 1, 0]
w_ = [1,1,1]
nn_modul.lernen(ergebnis_, y_, w_, 500)

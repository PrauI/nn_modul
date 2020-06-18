x = [[1, 0, 0], [1, 1, 0], [1, 0, 1], [1, 1, 1]]
y = [0, 1, 1, 1]
w = [-1, 1, 1]


def main(x1, w1, iter):
    for durchlauf in range(iter):
        y_hat = []
        zahl = []
        error = []
        k = 0
        for i in range(len(x1)):
            for d in range(len(x1[i])):
                k += x1[i][d] * w1[d]
            y_hat.append(k)

        summe = y_hat
        for i in summe:
            if i >= 0:
                zahl.append(1)
            else:
                zahl.append(0)
        return zahl

        for i in range(len(y1)):
            error.append(y1[i] - y_hat[i])

        for i in range(0, len(error)):
            if not error == 0:
                xd = x1[i]
                for e in range(len(xd)):
                    w[e] += xd[e] * error[e]

        if not durchlauf == iter:
            error.clear()
            zahl.clear()
        print("zahL", zahl)
        print("error", error)
        print("w", w)
    return zahl, error, w


g = main(x, w, 10)
print(g[0])
print(g[1])
print(g[2])

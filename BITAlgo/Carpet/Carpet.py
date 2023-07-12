from zad10ktesty import runtests

from math import inf


def carpet(N):
    # f(i) - najmniejsza ilosc dywanow aby osiągnać i metrów kwadratowych
    f = [0 for _ in range(N + 1)]
    parent = [None for _ in range(N + 1)]

    # g(i) - rozmiary dywanow skladajacych sie na rozwiazanie dla i metrow kwadratowych
    g = [[] for _ in range(N + 1)]

    f[0] = 0

    for i in range(1, N + 1):
        j = 1

        currMin = inf
        idx = None

        while i - j ** 2 >= 0:

            if f[i - j ** 2] < currMin:
                currMin = f[i - j ** 2]
                idx = i - j ** 2
                g[i] = g[i - j ** 2].copy()
                g[i].append(j)

            j += 1

        f[i] = currMin + 1
        parent[i] = idx

    return g[N]


runtests(carpet)

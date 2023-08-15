from egz1Atesty import runtests

from math import inf
from queue import PriorityQueue


def relax(u, v, l, d, parent, Q):
    if d[v] > d[u] + l:
        d[v] = d[u] + l
        parent[v] = u
        Q.put((d[v], v))


def Dijkstra(G, s):
    n = len(G)

    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]

    d[s] = 0
    Q = PriorityQueue()
    Q.put((0, s))

    while not Q.empty():
        du, u = Q.get()
        if du == d[u]:
            for v, l in G[u]:
                relax(u, v, l, d, parent, Q)

    return d


def transform(G, r):
    n = len(G)
    for i in range(n):
        for j in range(len(G[i])):
            G[i][j] = (G[i][j][0], G[i][j][1] * 2 + r)


def gold(G, V, s, t, r):
    n = len(G)

    # d[i] - najtańsza droga z zamku s do zamku i

    beforeRobbery = Dijkstra(G, s)  # d1
    transform(G, r)
    pastRobbery = Dijkstra(G, t)    # d2

    cost = inf
    for i in range(n):
        # d1[i] + d2[1] = suma kosztów przejazdów z zamku s do zamku t przy rabunku zamku i
        # V[i] = zysk z rabunku zamku i
        if beforeRobbery[i] + pastRobbery[i] - V[i] < cost:
            cost = beforeRobbery[i] + pastRobbery[i] - V[i]

    return cost


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests=True)

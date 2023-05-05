# Jan Kalęba

# Algorytm polega na klasycznym użyciu algorytmu Dijkstry.
# Ze względu na fakt, że między planetami przy
# osobliwościach można teleportować się w 0 czasie,
# planety te mogą być reprezentowane w grafie
# poprzez jedną makro-planetę - której
# lista sąsiadów znajduje się w Grafie na n-tej
# pozycji.
# Po wyjęciu wierzchołka b z kolejki, algorytm jest przerywany,
# ponieważ distance[b] zawiera już najkrótszą scieżkę z a do b.

# Aby uniknąć multikrawędzi między makro-planetą
# i niektórymi sąsiadami, krotki zawierająca
# indeksy i długości krawędzi są updateowane
# tak, aby między wierzchołkami grafu była zawsze
# maxymalnie 1 krawędź (czyli dwie krawedzie skierowane).

# Złożoność O((V + E + S) + ElogV) => O(V + S + ElogV)


from zad5testy import runtests

from math import inf
from queue import PriorityQueue


def transform(E: list[tuple[int]], n, S) -> tuple[list[list[tuple]], list[bool]]:
    # O(V)
    G = [[] for _ in range(n + 1)]
    teleport = [False for _ in range(n)]
    indices = [None for _ in range(n)]
    idx = 0

    # O(S)
    for i in range(len(S)):
        teleport[S[i]] = True

    # O(E)
    for e in E:
        v0, vk, distance = e[0], e[1], e[2]
        if teleport[v0]:
            if indices[vk] is None:
                G[n].append((vk, distance))
                G[vk].append((n, distance))
                indices[vk] = (idx, len(G[vk]) - 1)
                idx += 1
            else:
                idxInMacro = indices[vk][0]
                idxInPlanet = indices[vk][1]
                if distance < G[n][idxInMacro][1]:
                    newTuple = (G[n][idxInMacro][0], distance)
                    G[n][idxInMacro] = newTuple
                    newTuple2 = (G[vk][idxInPlanet][0], distance)
                    G[vk][idxInPlanet] = newTuple2

        elif teleport[vk]:
            if indices[v0] is None:
                G[n].append((v0, distance))
                G[v0].append((n, distance))
                indices[v0] = (idx, len(G[v0]) - 1)
                idx += 1
            else:
                idxInMacro = indices[v0][0]
                idxInPlanet = indices[v0][1]
                if distance < G[n][idxInMacro][1]:
                    newTuple = (G[n][idxInMacro][0], distance)
                    G[n][idxInMacro] = newTuple
                    newTuple2 = (G[v0][idxInPlanet][0], distance)
                    G[v0][idxInPlanet] = newTuple2

        else:
            G[v0].append((vk, distance))
            G[vk].append((v0, distance))

    return G, teleport


def relax(u, v, length, distance, Q):
    if distance[v] > distance[u] + length:
        distance[v] = distance[u] + length
        Q.put((distance[v], v))


def spacetravel(n, E, S, a, b):
    # O(V + E + S)
    Graph, Teleports = transform(E, n, S)

    # O(V)
    distance = [inf for _ in range(n + 1)]

    if Teleports[a]:
        a = n
    if Teleports[b]:
        b = n

    # O(ElogV)
    distance[a] = 0
    Q = PriorityQueue()
    Q.put((distance[a], a))
    while not Q.empty():
        du, u = Q.get()

        if du == distance[u]:
            for (v, l) in Graph[u]:
                relax(u, v, l, distance, Q)

    return distance[b] if distance[b] != inf else None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)

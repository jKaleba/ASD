# Złożoność O(VElog*E)


from kol2testy import runtests

from math import inf


class Node:
    def __init__(self, value):
        self.parent = self
        self.rank = 0
        self.value = value


def findset(x):
    if x.parent != x:
        x.parent = findset(x.parent)

    return x.parent


def union(x, y):
    x = findset(x)
    y = findset(y)

    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y

        if x.rank == y.rank:
            y.rank += 1


# O(Elog*V)
def MSTKruskal(Edges: list[tuple], start, n):
    MST = []
    V = [Node(i) for i in range(n)]

    outside = []

    for i in range(n):
        e = Edges[start + i]
        u, v, w = e
        if findset(V[u]) != findset(V[v]):
            union(V[u], V[v])
            MST.append(e)
        else:
            outside.append(e)

    return MST, outside


# O(V^2)
def transformToEdges(Graph: list[list[tuple]]):
    n = len(Graph)
    visited = [False for _ in range(n)]

    E = []

    # counter = 0

    for u in range(n):
        visited[u] = True

        # counter += len(Graph[u])

        for (v, w) in Graph[u]:
            if not (visited[u] and visited[v]):
                E.append((u, v, w))

    # print(counter)
    return E


def beautree(G):
    n = len(G)

    Edges = transformToEdges(G)

    # O(ElogE)
    Edges.sort(key=lambda tup: tup[2])
    eLen = len(Edges)

    # m < krawędzie w środku < M
    # m - minimalna
    # M - maksymalna
    # => MST po kolei aż zacznie brakować wierzchołków

    lightest = inf

    for i in range(eLen - n):
        mst, outside = MSTKruskal(Edges, i, n)

        if len(mst) != n - 1:
            continue

        m = min(mst, key=lambda tup: tup[2])[2]
        M = max(mst, key=lambda tup: tup[2])[2]

        minOutside = min(outside, key=lambda tup: tup[2])[2]
        maxOutside = max(outside, key=lambda tup: tup[2])[2]

        currSum = 0
        for j in range(len(mst)):
            currSum += mst[j][2]

        # print(mst)
        # print(minOutside, maxOutside, m, M)
        # print(outside)
        # input()

        if minOutside > M or maxOutside < m:
            lightest = min(currSum, lightest)
            # prawdopodobnie można tu przerwać, ze względu na fakt,
            # że wagi były od początku posortowane, więc
            # minimalne drzewo spełniajace warunki będzie
            # pierwszym jakie się pojawi

            return lightest

    # return lightest if lightest != inf else None
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(beautree, all_tests=True)

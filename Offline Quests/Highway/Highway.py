from zad8testy import runtests

from math import sqrt, ceil, inf


def distance(A, i, j):
    return ceil(sqrt((A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2))


class Node:
    def __init__(self, value):
        self.parent = self
        self.rank = 0
        self.value = value


def findSet(x: Node):
    while x.parent != x:
        x = x.parent

    return x.parent


def union(x: Node, y: Node):
    x = findSet(x)
    y = findSet(y)

    if x.rank > y.rank:
        y.parent = x

    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def Kruskal(E: list[tuple[int, int, int]], n, minDifference):
    V = [Node(i) for i in range(n)]

    edgeCounter = 0
    maxEdge = 0
    for idx, e in enumerate(E):
        u, v, w = e
        if findSet(V[u]) != findSet(V[v]):
            union(V[u], V[v])
            edgeCounter += 1
            maxEdge = max(maxEdge, w)

        if E[idx][2] - E[0][2] >= minDifference:
            break

    if edgeCounter == n - 1:
        minDifference = min(minDifference, maxEdge - E[0][2])

    return minDifference


def highway(A):
    n = len(A)

    Edges = []

    for i in range(n):
        for j in range(i + 1, n):
            Edges.append((i, j, distance(A, i, j)))

    Edges.sort(key=lambda x: x[2])

    minDifference = inf
    for i in range(len(Edges)):
        minDifference = Kruskal(Edges[i:], n, minDifference)

    return minDifference


runtests(highway, all_tests=True)

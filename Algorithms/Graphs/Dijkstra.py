from math import inf
from queue import PriorityQueue
from random import randint


def relax(u, v, length, distance, parent, Q):
    if distance[v] > distance[u] + length:
        distance[v] = distance[u] + length
        parent[v] = u
        Q.put((distance[v], v))


def DijkstraForList(Graph: list[list[tuple[int, int]]], s):
    n = len(Graph)
    parent = [None for _ in range(n)]
    distance = [inf for _ in range(n)]

    distance[s] = 0
    Q = PriorityQueue()
    Q.put((distance[s], s))

    while not Q.empty():
        du, u = Q.get()
        if du == distance[u]:
            # then it means the vertex hasn't been visited
            for (v, l) in Graph[u]:
                relax(u, v, l, distance, parent, Q)

    return distance, parent


def DijkstraForMatrix(Graph: list[list[int]], s):
    n = len(Graph)
    parent = [None for _ in range(n)]
    distance = [inf for _ in range(n)]

    distance[s] = 0
    Q = PriorityQueue()
    Q.put((0, s))

    while not Q.empty():
        du, u = Q.get()
        if du == distance[u]:
            for v in range(n):
                if Graph[u][v] != inf:
                    relax(u, v, Graph[u][v], distance, parent, Q)

    return distance, parent


def listToMatrix(Graph: list[list[tuple[int, int]]]):
    n = len(Graph)
    G = [[inf for _ in range(n)] for __ in range(n)]

    for u in range(n):
        for (v, l) in Graph[u]:
            G[u][v] = l

    return G


printGraph = lambda r: print(r)

if __name__ == '__main__':
    N = 15  # number of vertices
    List = [[] for _ in range(N)]

    for a in range(N):
        for b in range(a + 1, N):
            bias = randint(1, 20)

            if randint(1, 10) < 4:
                List[a].append((b, bias))
                List[b].append((a, bias))

    Matrix = listToMatrix(List)

    list(map(printGraph, List))
    print()
    list(map(printGraph, Matrix))

    vertex = randint(0, N - 1)

    disList, parList = DijkstraForList(List, vertex)
    disMatrix, parMatrix = DijkstraForMatrix(Matrix, vertex)

    print()
    print(disList)
    print(disMatrix)
    print()
    print(parList)
    print(parMatrix)

    print(disList == disMatrix and parList == parMatrix)

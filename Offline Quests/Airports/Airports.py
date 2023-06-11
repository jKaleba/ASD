from kol3btesty import runtests

from math import inf
from queue import PriorityQueue


def relax(u, v, length, distance, Q):
    if distance[v] > distance[u] + length:
        distance[v] = distance[u] + length
        Q.put((distance[v], v))


def DijkstraForList(Graph: list[list[tuple[int, int]]], s, t):
    n = len(Graph)
    distance = [inf for _ in range(n)]

    distance[s] = 0
    Q = PriorityQueue()
    Q.put((distance[s], s))

    while not Q.empty():
        du, u = Q.get()

        if u == t:
            break

        if du == distance[u]:
            # then it means the vertex hasn't been visited
            for (v, l) in Graph[u]:
                relax(u, v, l, distance, Q)

    return distance

# O(ElogV)
def airports1(G: list[list[tuple]], A, s, t):
    n = len(G)

    G.append([])

    for i in range(n):
        G[n].append((i, A[i]))
        G[i].append((n, A[i]))

    distance = DijkstraForList(G, s, t)

    return distance[t]

# O(E^2)
def airports2(G: list[list[tuple]], A, s, t):
    for u in range(len(A)):
        for v in range(len(A)):
            if u != v:
                G[u].append((v, A[u] + A[v]))

    distance = DijkstraForList(G, s, t)

    return distance[t]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(airports1, all_tests=True)

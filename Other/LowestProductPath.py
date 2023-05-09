from math import inf, log2
from queue import PriorityQueue
from random import randint


# Graf o najmniejszym iloczynie bedzie grafem o najmniejszej sumie
# logarytmow --> log(a * b * c) = log(a) + log(b) + log(c)
def graphOfLogarithms(Graph: list[list[tuple[int, int]]]):
    for u in range(len(Graph)):
        for idx in range(len(Graph[u])):
            v, l = Graph[u][idx]
            Graph[u][idx] = (v, log2(l))

    return Graph


####################################################
def relax(u, v, length, distance, parent, Q):
    if distance[v] > distance[u] + length:
        distance[v] = distance[u] + length
        parent[v] = u
        Q.put((distance[v], v))


def Dijkstra(Graph: list[list[tuple[int, int]]], s):
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


################################################################


def printPath(start, dest, parent):
    path = [dest]

    while dest != start:
        dest = parent[dest]
        path.append(dest)

    print(path[::-1])


def printPathR(start, dest, parent):
    if start != dest:
        printPathR(start, parent[dest], parent)

    print(f" {dest}", end=" ")


printGraph = lambda r: print(r)

if __name__ == '__main__':
    N = 15  # number of vertices
    G = [[] for _ in range(N)]

    for a in range(N):
        for b in range(a + 1, N):
            bias = randint(1, 20)

            if randint(1, 10) < 4:
                G[a].append((b, bias))
                G[b].append((a, bias))

    list(map(printGraph, G))

    vertex = randint(0, N - 1)

    while True:
        destination = randint(0, N - 1)
        if destination != vertex:
            break

    G = graphOfLogarithms(G)
    dis, par = Dijkstra(G, vertex)

    printPath(vertex, destination, par)
    printPathR(vertex, destination, par)

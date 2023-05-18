from queue import PriorityQueue
from math import inf
from random import randint


############################################################################################
# Find / Union Structure
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


# O(ElogE) & (E < V^2)
# ==>
# logE < (logV^2) = 2logV
# ==>
# O(ElogV)
def KruskalAlgorithm(E: list[tuple[int, int, int]], n):
    MST = []
    V = [Node(i) for i in range(n)]

    E.sort(key=lambda tup: tup[2])

    for e in E:
        u, v, w = e
        if findSet(V[u]) != findSet(V[v]):
            union(V[u], V[v])
            MST.append(e)

    return MST

############################################################################################

def relaxPrime(u: int, v: int, length: int, distance: list, parent: list, Q: PriorityQueue):
    if distance[v] > length:
        distance[v] = length
        parent[v] = u
        Q.put((distance[v], v))


# O(ElogV) -> it's basically Dijkstra with minor change in
# relaxation function -> instead of the absolute distance
# from start to current v, only current-edge distance
# is being taken into account.
def PrimAlgorithmReturningEdges(Graph: list[list[tuple[int, int]]]):
    n = len(Graph)

    MST = []

    parent = [None for _ in range(n)]
    distance = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    added = [False for _ in range(n)]

    # random start vertex -> can be specified if wanted
    v0 = randint(0, n - 1)

    Q = PriorityQueue()
    Q.put((0, v0))

    while not Q.empty():
        du, u = Q.get()

        if not visited[u]:
            for (v, l) in Graph[u]:
                relaxPrime(u, v, l, distance, parent, Q)

        if not added[u]:
            MST.append((parent[u], u, du))
            added[u] = True

    return MST

def PrimAlgorithmReturningTree(Graph: list[list[tuple[int, int]]]):
    n = len(Graph)

    MST = [[] for _ in range(n)]

    parent = [None for _ in range(n)]
    distance = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    added = [False for _ in range(n)]

    # random start vertex -> can be specified if wanted
    v0 = randint(0, n - 1)

    Q = PriorityQueue()
    Q.put((0, v0))

    while not Q.empty():
        du, u = Q.get()

        if not visited[u]:
            for (v, l) in Graph[u]:
                relaxPrime(u, v, l, distance, parent, Q)

        if not added[u] and parent[u] is not None:
            MST[parent[u]].append((u, du))
            MST[u].append((parent[u], du))
            added[u] = True
            added[parent[u]] = True

    return MST

############################################################################################

def transform(E, n):
    G = [[] for _ in range(n)]
    for e in E:
        u, v, w = e
        G[u].append((v, w))
        G[v].append((u, w))

    return G


if __name__ == '__main__':
    N = 7  # number of vertices

    Edges = [
        (0, 1, 5),
        (1, 2, 21),
        (1, 3, 1),
        (2, 4, 7),
        (3, 4, 13),
        (3, 5, 16),
        (4, 6, 4),
        (5, 6, 1)
    ]
    print("Kruskal:")
    mst = KruskalAlgorithm(Edges, N)
    kruskalSum = primSum = 0
    for edge in mst:
        print(edge[0], edge[1])
        kruskalSum += edge[2]

    print("\nPrim:")
    Gr = transform(Edges, N)
    mst2 = PrimAlgorithmReturningEdges(Gr)
    for edge in mst2:
        print(edge[0], edge[1])
        primSum += edge[2]

    print("\nPrim v2:")
    mstTree = PrimAlgorithmReturningTree(Gr)
    for row in mstTree:
        print(row)
    print()
    
    print(f"KruskalSum: {kruskalSum} & PrimSum: {primSum}")

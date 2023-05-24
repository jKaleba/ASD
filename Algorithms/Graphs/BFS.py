from queue import Queue


# Breadth-First Search
def BFS_List(Graph: list[list[int]], s):
    n = len(Graph)
    Q = Queue()

    d = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    Q.put(s)
    parent[s] = None
    visited[s] = True
    d[s] = 0

    while not Q.empty():
        u = Q.get()
        for v in Graph[u]:
            if not visited[v]:
                d[v] = d[u] + 1
                parent[v] = u
                visited[v] = True
                Q.put(v)

    return d, parent, visited
def BFS_Matrix(Graph: list[list[int]], s):
    n = len(Graph)
    Q = Queue()

    d = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    Q.put(s)
    parent[s] = None
    visited[s] = True
    d[s] = 0

    while not Q.empty():
        u = Q.get()
        for v in range(n):
            if Graph[u][v] and not visited[v]:
                d[v] = d[u] + 1
                parent[v] = u
                visited[v] = True
                Q.put(v)

    return d, parent, visited


def listToMatrix(Graph: list[list[int]]):
    n = len(Graph)
    M = [[False for _ in range(n)] for __ in range(n)]

    for u in range(n):
        for v in Graph[u]:
            M[u][v] = True

    return M


if __name__ == '__main__':
    G = [
        [0, 1],
        [1, 0, 2, 3],
        [2, 1, 3, 4],
        [3, 1, 2, 4],
        [4, 1, 2, 3]
    ]

    res = BFS_List(G, 1)
    print(res[0])
    print(res[1])
    print(res[2])
    print()

    res = BFS_Matrix(listToMatrix(G), 1)
    print(res[0])
    print(res[1])
    print(res[2])

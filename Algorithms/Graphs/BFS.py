from queue import Queue


# Breadth-First Search
def BFS(Graph: list[list[int]], s):
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
        for v in range(len(Graph[u])):
            x = Graph[u][v]
            if not visited[x]:
                d[x] += 1
                parent[v] = u
                visited[x] = True
                Q.put(x)

    return d, parent, visited


if __name__ == '__main__':
    G = [
        [0, 1],
        [1, 0, 2, 3],
        [2, 1, 3, 4],
        [3, 1, 2, 4],
        [4, 1, 2, 3]
    ]

    res = BFS(G, 1)
    print(res[0])
    print(res[1])
    print(res[2])

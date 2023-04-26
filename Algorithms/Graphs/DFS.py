# Depth-First Search
# Complexity:
# O(V + E) -> list representation
# O(V^2) -> matrix representation

def DFS(Graph: list[list[int]], s):
    n = len(Graph)
    time = 0

    def DFSVisit(G: list[list[int]], u):
        nonlocal time

        visited[u] = True
        time += 1
        visitTime[u] = time

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFSVisit(G, v)

        time += 1
        return

    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    visitTime = [-1 for _ in range(n)]

    for i in range(n):
        if not visited[i]:
            DFSVisit(Graph, i)

    return visited, parent, visitTime


if __name__ == '__main__':
    Gr = [
        [0, 1],
        [1, 0, 3],
        [2, 1, 3, 4],
        [3, 1, 2, 4],
        [4, 1, 2, 3]
    ]

    res = DFS(Gr, 1)

    print([i for i in range(len(Gr))])
    print(res[0])
    print(res[1])
    print(res[2])

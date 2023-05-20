# Depth-First Search
# Complexity:
# O(V + E) -> list representation
# O(V^2) -> matrix representation

from collections import deque


def DFS_List(Graph: list[list[int]], s):
    n = len(Graph)
    time = 0

    def DFSVisit(u):
        nonlocal time

        visited[u] = True
        time += 1
        visitTime[u] = time

        for v in Graph[u]:
            if not visited[v]:
                parent[v] = u
                DFSVisit(v)

        time += 1
        return

    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    visitTime = [-1 for _ in range(n)]

    for neighbor in Graph[s]:
        DFSVisit(neighbor)

    return visited, parent, visitTime


def DFS_List_Iter(Graph: list[list[int]], s):
    n = len(Graph)
    time = 0

    def DFSVisit(source):
        nonlocal time

        Stack = deque()
        Stack.append(source)

        while Stack:
            u = Stack.pop()
            visited[u] = True
            time += 1
            visitTime[u] = time

            for v in Graph[u]:
                if not visited[v]:
                    parent[v] = u
                    Stack.append(v)

            time += 1
        return

    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    visitTime = [-1 for _ in range(n)]

    DFSVisit(s)

    return visited, parent, visitTime


def DFS_Matrix(Graph: list[list[bool]], s):
    n = len(Graph)
    time = 0

    def DFSVisit(u):
        nonlocal time

        visited[u] = True
        time += 1
        visitTime[u] = time

        for v in range(len(Graph[u])):
            if Graph[u][v] and not visited[v]:
                parent[v] = u
                DFSVisit(v)

        time += 1
        return

    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    visitTime = [-1 for _ in range(n)]

    DFSVisit(s)

    return visited, parent, visitTime


def listToMatrix(Graph: list[list[bool]]):
    n = len(Graph)
    G = [[False for _ in range(n)] for __ in range(n)]

    for u in range(n):
        for v in Graph[u]:
            G[u][v] = True

    return G


if __name__ == '__main__':
    Gr = [
        [0, 1],
        [1, 0, 3],
        [2, 1, 3, 4],
        [3, 1, 2, 4],
        [4, 1, 2, 3]
    ]

    res = DFS_List(Gr, 1)

    print([i for i in range(len(Gr))])
    print()
    print(res[0])
    print(res[1])
    print(res[2])

    res2 = DFS_List_Iter(Gr, 1)
    print()
    print(res2[0])
    print(res2[1])
    print(res2[2])

    res3 = DFS_Matrix(listToMatrix(Gr), 1)
    print()
    print(res2[0])
    print(res2[1])
    print(res2[2])

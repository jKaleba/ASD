from copy import deepcopy

from zad9testy import runtests

from collections import deque


def FordFulkerson_Matrix(Matrix: list[list[int]], s: int, t: int):
    def minWeight(Graph: list[list[int]], path: list[int]):
        minW = Graph[path[0]][path[1]]
        for i in range(1, len(path) - 1):
            minW = min(minW, Graph[path[i]][path[i + 1]])

        return minW

    def updateWeights(Graph: list[list[int]], path: list[int], minW: int):
        for i in range(len(path) - 1):
            Graph[path[i]][path[i + 1]] -= minW
            Graph[path[i + 1]][path[i]] += minW

        return

    def augmentingPath(Graph: list[list[int]], source: int, sink: int):
        n = len(Graph)
        visited = [False for _ in range(n)]
        parent = [None for _ in range(n)]
        Stack = deque()

        Stack.append(source)
        visited[source] = True

        while Stack:
            u = Stack.pop()
            for v in range(n):
                if Graph[u][v] and not visited[v]:
                    Stack.append(v)
                    visited[v] = True
                    parent[v] = u

        path = []
        if visited[sink]:
            v = sink
            while v != source:
                path.append(v)
                v = parent[v]
            path.append(source)
            path.reverse()

        return path

    ###########################################################################

    count = 0
    augPath = augmentingPath(Matrix, s, t)
    while augPath:
        minW = minWeight(Matrix, augPath)
        updateWeights(Matrix, augPath, minW)
        count += minW
        augPath = augmentingPath(Matrix, s, t)

    return count


def merge(Matrix: list[list[int]], a: int, b: int) -> list[list[int]]:
    n = len(Matrix)
    for i in range(n):
        Matrix[i][b] += Matrix[i][a]
        Matrix[i][a] = 0
    return Matrix


def transform(E):
    size = 0
    for e in E:
        size = max(size, e[0], e[1])

    size += 1

    Graph = [[0 for _ in range(size)] for __ in range(size)]

    for e in E:
        Graph[e[0]][e[1]] = e[2]

    return Graph


def toList(Matrix: list[list[int]]) -> list[list[tuple[int, int]]]:
    n = len(Matrix)
    List = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if Matrix[i][j] != -1:
                List[i].append((j, Matrix[i][j]))

    return List


def sumOfInput(G, x, y):
    result = 0
    for i in range(len(G)):
        result += G[i][x] + G[i][y]

    return result


def maxflow(E, s):
    Graph = transform(E)

    sumOutput = 0

    for e in E:
        if e[0] == s:
            sumOutput += e[2]

    n = len(Graph)
    maxFlow = 0
    for i in range(n):
        for j in range(i + 1, n):
            if i != s and j != s:
                G = deepcopy(Graph)

                if sumOfInput(G, i, j) <= maxFlow:
                    continue

                G = merge(G, i, j)

                flow = FordFulkerson_Matrix(G, s, j)

                maxFlow = max(maxFlow, flow)

                if sumOutput == maxFlow:
                    return maxFlow

    # input()

    return maxFlow


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxflow, all_tests=True)

from collections import deque
from copy import deepcopy


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


def FordFulkerson_List(List: list[tuple[int, int]], s: int, t: int):
    def updateWeights(Graph: list[tuple[int, int]], path: list[int], minW: int):
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            for idx, (vertex, flow) in enumerate(Graph[u]):
                if vertex == v:
                    Graph[u][idx] = (vertex, flow - minW)
                    break

            for idx, (vertex, flow) in enumerate(Graph[v]):
                if vertex == u:
                    Graph[v][idx] = (vertex, flow + minW)
                    break

    def augmentingPath(Graph: list[tuple[int, int]], source: int, sink: int):
        n = len(Graph)
        visited = [False for _ in range(n)]
        parent = [None for _ in range(n)]

        # flow between vertex v and u = parent[v]
        flowBetween = [0 for _ in range(n)]
        Stack = deque()

        Stack.append(source)
        visited[source] = True

        while Stack:
            u = Stack.pop()
            for idx, (v, f) in enumerate(Graph[u]):
                if f and not visited[v]:
                    Stack.append(v)
                    visited[v] = True
                    parent[v] = u
                    flowBetween[v] = f

        path = []
        minW = 0
        if visited[sink]:
            v = sink
            minW = flowBetween[v]  # same result as float('inf')
            while v != source:
                path.append(v)
                minW = min(minW, flowBetween[v])
                v = parent[v]
            path.append(source)
            path.reverse()

        return path, minW

    ###########################################################################

    count = 0
    augPath, minW = augmentingPath(List, s, t)
    while augPath:
        updateWeights(List, augPath, minW)
        count += minW
        augPath, minW = augmentingPath(List, s, t)

    return count


def matrixToList(Matrix: list[list[int]]) -> list[list[tuple[int, int]]]:
    n = len(Matrix)
    List = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if Matrix[i][j]:
                List[i].append((j, Matrix[i][j]))

    return List


if __name__ == '__main__':

    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]

    for i in range(5):
        for j in range(0, 5):
            if i == j:
                continue

            M = deepcopy(graph)
            L = matrixToList(M)

            resultMatrix = FordFulkerson_Matrix(M, i, j)
            resultList = FordFulkerson_List(L, i, j)

            if resultMatrix != resultList:
                print('Error')
                break
            else:
                print(f'Sink - {i}, Source - {j}, Max Flow - {resultMatrix}')

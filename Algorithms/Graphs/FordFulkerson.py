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

    count = 0
    augPath = augmentingPath(Matrix, s, t)
    while augPath:
        minW = minWeight(Matrix, augPath)
        updateWeights(Matrix, augPath, minW)
        count += minW
        augPath = augmentingPath(Matrix, s, t)

    return count


if __name__ == '__main__':

    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]

    print(FordFulkerson_Matrix(graph, 0, 5))

from random import randint
from queue import Queue


def Euler(Graph):
    n = len(Graph)
    visited = [False for _ in range(n)]
    oddWeights = 0
    verticesLeft = n

    Q = Queue()
    Q.put(0)

    while not Q.empty():
        u = Q.get()

        oddWeights += len(Graph[u]) % 2
        verticesLeft -= 1

        for v in Graph[u]:
            if not visited[v]:
                visited[v] = True
                Q.put(v)

        visited[u] = True

    return oddWeights == 0 and verticesLeft == 0, (oddWeights == 2 or oddWeights == 0) and verticesLeft == 0


if __name__ == '__main__':
    N = 15  # number of vertices

    G = [
        [1, 13],  # neighbors of vertex 0
        [0, 2],  # neighbors of vertex 1
        [1, 3],  # neighbors of vertex 2
        [2, 4],  # neighbors of vertex 3
        [3, 5],  # neighbors of vertex 4
        [4, 6],  # neighbors of vertex 5
        [5, 7],  # neighbors of vertex 6
        [6, 8],  # neighbors of vertex 7
        [7, 9],  # neighbors of vertex 8
        [8, 10],  # neighbors of vertex 9
        [9, 11, 12, 14],  # neighbors of vertex 10
        [10, 12, 13, 14],  # neighbors of vertex 11
        [10, 11, 13, 14],  # neighbors of vertex 12
        [0, 11, 12, 14],  # neighbors of vertex 13
        [10, 11, 12, 13]  # neighbors of vertex 14
    ]

    cycle, path = Euler(G)
    print(cycle, path)

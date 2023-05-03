# Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem,
# jeżeli każdy inny wierzchołek można osiągnąć ścieżką skierowaną
# wychodzącą z v. Podać algorytm, który dla podanego grafu stwierdza,
# czy G posiada dobry początek.


###############################################################

def goodBeginning(Graph: list[list[int]]) -> bool:
    INVALID_TIME = -1
    n = len(Graph)

    visitTime = [INVALID_TIME for _ in range(n)]
    visited = [False for _ in range(n)]
    time = 1

    for u in range(n):
        if not visited[u]:
            time = DFSVisit(Graph, u, time, visitTime, visited)

    maxV = visitTime.index(len(Graph))

    for u in range(n):
        visitTime[u] = INVALID_TIME
        visited[u] = False

    DFSVisit(Graph, maxV, time, visitTime, visited)
    for vis in visited:
        if not vis:
            return False

    return True


def DFSVisit(Graph, u, time, visitTime, visited):
    visited[u] = True
    for v in Graph[u]:
        if not visited[v]:
            time = DFSVisit(Graph, v, time, visitTime, visited)

    visitTime[u] = time
    time += 1
    return time


###############################################################

def topologicalSort(Graph: list[list[int]]):
    n = len(Graph)
    visited = [False for _ in range(n)]
    sortedGraph = [0 for _ in range(n)]
    idx = n - 1

    def DFS(u):
        nonlocal idx

        visited[u] = True
        for v in Graph[u]:
            if not visited[v]:
                DFS(v)
        sortedGraph[idx] = u
        idx -= 1

    for i in range(n):
        if not visited[i]:
            DFS(i)

    return sortedGraph


def goodBeginning2(Graph: list[list[int]]) -> bool:
    # 1. Strongly Connected Components
    # 2. Edges reversion.
    # 3. Topological Sort
    # 4. Only the last one can possibly be good beginning.
    return False

###############################################################


if __name__ == '__main__':
    Gr = [
        [1, 2, 3],  # Node 0 has edges to nodes 1, 2, and 3
        [4, 5],  # Node 1 has edges to nodes 4 and 5
        [4, 7, 8],  # Node 2 has edges to nodes 4, 7, and 8
        [5, 9],  # Node 3 has edges to nodes 5 and 9
        [6, 7, 9],  # Node 4 has edges to nodes 6, 7, and 9
        [8, 10],  # Node 5 has edges to nodes 8 and 10
        [8, 10, 12],  # Node 6 has edges to nodes 8, 10, and 12
        [9, 11, 12, 13],  # Node 7 has edges to nodes 9, 11, 12, and 13
        [10, 13],  # Node 8 has edges to nodes 10 and 13
        [11, 14],  # Node 9 has edges to nodes 11 and 14
        [12, 14],  # Node 10 has edges to nodes 12 and 14
        [13, 14],  # Node 11 has edges to nodes 13 and 14
        [13],  # Node 12 has an edge to node 13
        [14],  # Node 13 has an edge to node 14
        []  # Node 14 has no outgoing edges (it is a sink)
    ]

    print(goodBeginning(Gr))

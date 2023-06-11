# Jan Kalęba

# Algorytm polega na zastosowaniu metody Forda-Fulkersona
# na grafie dwudzielnym stworzonym za pomocą macierzy M,
# do którego następnie dodawane jest źródło i ujście
# (odpowiednio na pozycji 2n i 2n+1).
# Wartość największego przepływu tego grafu będzie jednocześnie
# najliczniejszym skojarzeniem - czyli najliczniejszym
# dopasowaniem do siebie pracowników i prac.
# Przepływ na poszczególnych krawędziach jest reprezentowany przez
# wartości bool.

# Zlożoność O(V^3)


from zad6testy import runtests
from collections import deque


def updateWeights(Graph: list[list[tuple]], path):
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i + 1]

        for j in range(len(Graph[u])):
            if Graph[u][j][0] == v:
                Graph[u][j] = (Graph[u][j][0], False)
                break
        for j in range(len(Graph[v])):
            if Graph[v][j][0] == u:
                Graph[v][j] = (Graph[v][j][0], True)
                break


def findPath(Graph: list[list[tuple]], s, t):
    n = len(Graph)

    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    ## DFS Visit ##
    Stack = deque()
    Stack.append(s)
    while Stack:
        u = Stack.pop()
        visited[u] = True

        if visited[t]:
            break

        for (v, f) in Graph[u]:
            if not visited[v] and f:
                parent[v] = u
                Stack.append(v)
    ################

    path = []
    if parent[t] is None:
        return None

    while t is not None:
        path.append(t)
        t = parent[t]
    path.reverse()
    return path


def FordFulkerson(Graph, s, t):
    count = 0

    augmentingPath = findPath(Graph, s, t)
    while augmentingPath:
        count += 1
        updateWeights(Graph, augmentingPath)
        augmentingPath = findPath(Graph, s, t)

    return count


def binworker(M: list[list]):
    n = len(M)
    Graph = [[] for _ in range(2 * n)]
    Graph.append([])  # s
    Graph.append([])  # t

    for i in range(n):
        for j in range(len(M[i])):
            Graph[i].append((M[i][j] + n, True))
            Graph[M[i][j] + n].append((i, False))

    for i in range(n):
        if len(Graph[i]):
            Graph[2 * n].append((i, True))
            Graph[i].append((2 * n, False))

        if len(Graph[n + i]):
            Graph[n + i].append((2 * n + 1, True))
            Graph[2 * n + 1].append((n + 1, False))

    return FordFulkerson(Graph, 2 * n, 2 * n + 1)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(binworker, all_tests=True)

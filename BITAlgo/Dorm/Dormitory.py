from egzP7atesty import runtests

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


def akademik(T):
    n = len(T)

    G = [[] for _ in range(2 * n)]
    G.append([])  # s
    G.append([])  # t

    # 0..n - 1 => studenci
    # n..2n - 1 => pokoje
    # 2n => s
    # 2n + 1 => t

    for idx, v in enumerate(T):
        for x in v:
            if x is not None:
                G[idx].append((n + x, True))
                G[n + x].append((idx, False))

    noPreferences = 0
    for i in range(n):
        if len(G[i]):
            G[2 * n].append((i, True))
            G[i].append((2 * n, False))
        else:
            noPreferences += 1

        if len(G[n + i]):
            G[n + i].append((2 * n + 1, True))
            G[2 * n + 1].append((n + i, False))

    return n - FordFulkerson(G, 2 * n, 2 * n + 1) - noPreferences


runtests(akademik)

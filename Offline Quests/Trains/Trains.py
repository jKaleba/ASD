from math import inf

from egzP5btesty import runtests


# O(nlogn)
def transform(B):
    for idx in range(len(B)):
        x, y = B[idx]
        if x > y:
            B[idx] = (y, x)

    B = sorted(B, key=lambda x: (x[1], x[0]))

    n = max(B, key=lambda x: x[1])[1] + 1

    G = [[] for _ in range(n)]

    x, y = B[0]
    G[x].append(y)
    G[y].append(x)

    for idx in range(1, len(B)):
        if B[idx][0] != B[idx - 1][0] or B[idx][1] != B[idx - 1][1]:
            x, y = B[idx]
            G[x].append(y)
            G[y].append(x)

    return G


# O(V + E) -> O(n + n) -> O(n)
def DFS_List(Graph: list[list[int]], s):
    n = len(Graph)

    # Current time
    time = 0

    def DFSVisit(u):
        nonlocal time

        visited[u] = True
        time += 1
        low[u] = visitTime[u] = time

        # Children of current node in DFS tree <=> neighbors && unvisited
        children = 0

        for v in Graph[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                DFSVisit(v)

                # Update low value of u for parent function calls
                low[u] = min(low[u], low[v])

                if low[v] >= visitTime[u] and parent[u] is not None:
                    articulationPoint[u] = True
                elif parent[u] is None and children > 1:
                    articulationPoint[u] = True

            # Backward edge in DFS tree
            elif v != parent[u]:
                low[u] = min(low[u], visitTime[v])

        return

    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    visitTime = [-1 for _ in range(n)]

    # low(v) - cycle indentifier
    low = [inf for _ in range(n)]
    # ap(v) - boolean array whether v is articulation point or not
    articulationPoint = [False for _ in range(n)]

    for neighbor in Graph[s]:
        DFSVisit(neighbor)

    return articulationPoint


def koleje(B):
    # O(nlogn)
    G = transform(B)

    # O(n)
    articulationPoints = DFS_List(G, 0)

    return sum(articulationPoints)


runtests(koleje, all_tests=True)

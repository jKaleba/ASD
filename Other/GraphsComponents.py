def dfs_visit(G, u, visited):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            dfs_visit(G, v, visited)


def components(G: list[list[int]]) -> int:
    n = len(G)

    visited = [False for _ in range(n)]
    count = 0

    for i in range(n):
        if not visited[i]:
            dfs_visit(G, i, visited)
            count += 1

    return count


if __name__ == '__main__':
    Gr = [
        [1],
        [0, 3],
        [1, 3, 4],
        [1, 2, 4],
        [1, 2, 3],
        [],
        [],
        [8],
        [7],
        []
    ]

    print(components(Gr))

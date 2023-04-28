def hasCycleOfLength4(Graph: list[list[int]]) -> bool:
    n = len(Graph)

    for u in range(n):
        for v in range(n):
            counter = 0
            for i in range(n):
                if i != u and i != v:
                    if Graph[v][i] and Graph[u][i]:
                        counter += 1

            if counter >= 2:
                return True

    return False


##########################################################
# Whether Gr is directional or not, it will be transformed
# properly.
def transformToMatrix(Graph: list[list[int]]) -> list[list]:
    n = len(Graph)
    G = [[0 for _ in range(n)] for __ in range(n)]

    for u in range(n):
        for v in Graph[u]:
            G[u][v] = 1

    return G


def transformToList(Graph: list[list[int]]) -> list[list]:
    n = len(Graph)
    G = [[] for _ in range(n)]

    for i in range(n):
        for j in range(0, n):
            if Graph[i][j]:
                G[i].append(j)

    return G
##########################################################


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

    Gr = transformToMatrix(Gr)
    for row in Gr:
        print(row)

    print(f"\n{hasCycleOfLength4(Gr)}\n")

    Gr = transformToList(Gr)
    for row in Gr:
        print(row)
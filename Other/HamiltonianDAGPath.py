from Algorithms.Graphs.TopologicalSort import topologicalSort


def hamiltonianDAGPath(DAG: list[list[int]]):

    # O(V + E)
    sortedGraph = topologicalSort(DAG)
    n = len(sortedGraph)

    # O(E)
    for i in range(n - 1):
        u = sortedGraph[i]
        v = sortedGraph[i + 1]

        if v not in DAG[u]:
            return False

    return True


if __name__ == '__main__':
    Gr = [
        [1, 2, 3],
        [2, 4, 5],
        [3, 4, 7, 8],
        [4, 5, 9],
        [5, 6, 7, 9],
        [6, 8, 10],
        [7, 8, 10, 12],
        [8, 9, 11, 12, 13],
        [9, 10, 13],
        [10, 11, 14],
        [11, 12, 14],
        [12, 13, 14],
        [13],
        [14],
        []
    ]

    print(hamiltonianDAGPath(Gr))

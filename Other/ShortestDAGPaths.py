from math import inf
import random


def findPaths(Graph: list[list[tuple[int, int]]], s):
    n = len(Graph)
    SortedGraph = topologicalSort(Graph)
    distance = [inf for _ in range(n)]
    parent = [None for _ in range(n)]

    distance[s] = 0

    # O(E)
    for idx in range(SortedGraph.index(s), n):
        for vertex, weight in Graph[SortedGraph[idx]]:
            if distance[vertex] > distance[SortedGraph[idx]] + weight:
                distance[vertex] = distance[SortedGraph[idx]] + weight
                parent[vertex] = SortedGraph[idx]

    return distance, parent


# O(V + E)
def topologicalSort(Graph: list[list[tuple[int, int]]]):
    n = len(Graph)
    visited = [False for _ in range(n)]
    sortedGraph = [0 for _ in range(n)]
    idx = n - 1

    def DFS(u):
        nonlocal idx

        visited[u] = True
        for v, b in Graph[u]:
            if not visited[v]:
                DFS(v)
        sortedGraph[idx] = u
        idx -= 1

    for i in range(n):
        if not visited[i]:
            DFS(i)

    return sortedGraph


if __name__ == '__main__':

    num_vertices = 15

    # Create an empty list for each node in the graph
    DAG = [[] for _ in range(num_vertices)]

    # Add random edges with biases to the graph
    for a in range(num_vertices):
        for b in range(a + 1, num_vertices):
            if random.random() < 0.3:
                bias = random.randint(1, 20)
                DAG[a].append((b, bias))

    # Print the resulting DAG
    for row in DAG:
        print(row)
    print()

    dist, par = findPaths(DAG, 0)
    print(dist)
    print(par)

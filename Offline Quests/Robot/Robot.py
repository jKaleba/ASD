from egzP8btesty import runtests

from math import inf


def FloydWarshall(graph):
    V = len(graph)
    distances = [[inf for j in range(V)] for i in range(V)]

    # Inicjalizacja macierzy odległości na podstawie grafu
    for u in range(V):
        distances[u][u] = 0

        for v, weight in graph[u]:
            if u != v:
                distances[u][v] = weight

    # Wykonanie relaksacji dla wszystkich par wierzchołków
    for k in range(V):
        for u in range(V):
            for v in range(V):
                distances[u][v] = min(distances[u][v], distances[u][k] + distances[k][v])

    return distances


def robot(G, P):
    result = 0
    matrix = FloydWarshall(G)
    point = P[0]

    for j in P:
        result += matrix[point][j]
        point = j

    return result


runtests(robot, all_tests=True)

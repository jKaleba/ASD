from math import inf

# Złożoność: O(V^3)
def FloydWarshall(graph):
    V = len(graph)
    distances = [[inf for j in range(V)] for i in range(V)]

    # Inicjalizacja macierzy odległości
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

# Jan Kalęba

# Algorytm polega na dwukrotnym przeszukiwaniu grafu wszerz.
# Za pierwszym razem, graf jest przeszukiwany do momentu
# natrafienia na wierzchołek t.
# Za drugim razem, przeszukujemy go wstecz, zaczynając od t,
# i zaznaczając które wierzchołki były elementami najkrótszych ścieżek.
# Jeśli istnieje wierzchołek, do którego wchodzą wszystkie
# najkrótsze ścieżki, usunięcie jego i jego parenta powoduje, że
# najkrótsza ścieżka zostanie wydłużona.
# W przeciwnym przypadku, gdy parent nie istnieje lub nie ma
# wierzchołka skupiającego najkrótsze ścieżki, zadanie nie ma rozwiązania,
# więc zwracane jest None.

# Złożoność O(V + E)


from zad4testy import runtests

from queue import Queue


def longer(G, s, t):
    n = len(G)
    Q = Queue()

    UNVISITED = 0
    IN_QUEUE = 1
    VISITED = 2
    SHORTEST_PATH_ELEMENT = 3

    distance = [-1 for _ in range(n)]
    state = [UNVISITED for _ in range(n)]
    parent = [None for _ in range(n)]

    Q.put(s)
    state[s] = IN_QUEUE
    distance[s] = 0
    while not Q.empty():
        u = Q.get()

        if u == t:
            break

        for v in range(len(G[u])):
            x = G[u][v]
            if state[x] < IN_QUEUE:
                distance[x] = distance[u] + 1
                parent[x] = u
                state[x] = IN_QUEUE
                Q.put(x)

        state[u] = VISITED

    R = Queue()
    R.put(t)
    while not R.empty():
        u = R.get()
        path_elements = 0
        for v in range(len(G[u])):
            x = G[u][v]
            if state[x] == VISITED and distance[x] == distance[u] - 1:
                state[x] = SHORTEST_PATH_ELEMENT
                path_elements += 1
                R.put(x)
        if path_elements >= 1 and R.qsize() == 1:
            return parent[u], u

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
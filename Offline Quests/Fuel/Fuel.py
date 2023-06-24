# Jan Kalęba

# Algorytm zaczyna się od rekurencyjnego przejścia po
# (### edit ### -> rekurencja zamieniona na stos ###)
# tablicy znajdując całkowite rozmiary plam paliwa,
# które zaczynają się na dordze - na górnej krawędzi
# (jeżeli kilka części jednej plamy się na niej znajduje,
# to suma jest wpisywana jedynie do pierwszej takiej komórki).
# Następnie cysterna jest tankowana za pomocą ropy z wyliczonej
# wartości plamy w miejscu startu.
# Po starcie, cysterna jedzie po współrzędnych (0, i), dodając do
# kolejki priorytetowej wartość każdej napotkanej plamy,
# aż do momentu, gdy jej paliwo będzie ujemne - co oznacza, że potrzebne
# było zatankowanie przed danym punktem. Wtedy wybiera największą
# wartość z kolejki oraz zwiększa licznik postojów.
# Po przejściu całej linii licznik będzie wskazywał najmniejszą wymaganą liczbę postojów.

# Złożoność: O(m * n + mlogm)

from zad8testy import runtests

from queue import PriorityQueue, Queue


def visit(T, i, j, visited):
    n = len(T)
    m = len(T[0])

    visited[i][j] = True

    s = T[i][j]
    A = [1, -1, 0, 0]
    B = [0, 0, 1, -1]

    for k in range(len(A)):
        #              Indices in range                               Visited                    Value != 0
        if 0 <= i + A[k] < n and 0 <= j + B[k] < m and not visited[i + A[k]][j + B[k]] and T[i + A[k]][j + B[k]] != 0:
            s += visit(T, i + A[k], j + B[k], visited)

    return s


def visit2(T, i, j, visited):
    n = len(T)
    m = len(T[0])

    s = 0
    A = [1, -1, 0, 0]
    B = [0, 0, 1, -1]

    Stack = Queue()
    Stack.put((i, j))
    visited[i][j] = True

    while not Stack.empty():
        a, b = Stack.get()
        s += T[a][b]

        for k in range(len(A)):
            if 0 <= a + A[k] < n and 0 <= b + B[k] < m and not visited[a + A[k]][b + B[k]] and T[a + A[k]][b + B[k]] != 0:
                Stack.put((a + A[k], b + B[k]))
                visited[a + A[k]][b + B[k]] = True

    return s

def plan(T):
    n = len(T)
    m = len(T[0])

    # O(m * n)
    visited = [[False for _ in range(m)] for __ in range(n)]

    # O(m * n)
    for i in range(m):
        if not visited[0][i] and T[0][i] != 0:
            T[0][i] = visit2(T, 0, i, visited)
        else:
            T[0][i] = 0

    # O(mlogm)
    Q = PriorityQueue()
    fuel = T[0][0]

    stops = 1
    for i in range(1, m):
        fuel -= 1
        if fuel < 0:
            fuel += Q.get() * (-1)
            stops += 1

        if T[0][i] != 0:
            Q.put(T[0][i] * (-1))

    return stops


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)

# Jan Kalęba

# Algorytm polega na stworzeniu funkcji f analogicznej do polecenia zadania.
# Uzupełniany jest przypadek brzegowy dla pierwszego wieżowca - obliczany
# jest jego dystans do każdej działki.
# Następnie dla każdego następnego wieżowca, dla każdego j,
# przypisywana jest działka o indeksie j,
# wyliczany jest dystans między danym wieżowcem i działką, a następnie
# znajdowany minimumm spośród sum dystansów dla poprzedniego wieżowca i
# możliwych zajętych przez niego działek, czyli tych z przedziału [0, j - 1].
# Obliczona wartość jest zwiększana o aktualny dystans i zapisywana na pozycji (i, j).
# Wynikiem jest minimum z sum dystansów dla ostatnigo wieżowca.

# Złożoność obliczeniowa: O(n^3)
# Złożoność pamięciowa: O(n^2)


from egz2btesty import runtests

from math import inf


def distance(X, Y, i, j):
    return abs(X[i] - Y[j])


def parking(X, Y):
    n = len(X)
    m = len(Y)

    # f(i, j) - minimalna suma odleglosci buirtowcow z pozycji
    # X[0] .. X[i] oraz do przydzielonych ich działek,
    # przy założeniu że biurowiec z pozycji X[i] ma przydzieloną
    # działkę z pozycji Y[j]

    #           działki            wieżowce
    f = [[inf for _ in range(m)] for _ in range(n)]

    # f(0, j) = |X[0] - Y[j]|
    for j in range(m):
        f[0][j] = distance(X, Y, 0, j)

    for i in range(1, n):
        for j in range(m):
            currDistance = distance(X, Y, i, j)

            for k in range(j):
                f[i][j] = min(f[i][j], f[i - 1][k] + currDistance)

    return min(f[n - 1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)

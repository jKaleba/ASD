# Jan Kalęba

# Złożoność obliczeniowa: O(n)
# Złożoność pamięciowa: O(n)

from egz2atesty import runtests


def dominance(P):
    n = len(P)

    # G[i] - liczba punktów takich ze x >= i
    G = [0 for _ in range(n + 1)]
    # T[i] - liczba punktów takich ze y >= i
    T = [0 for _ in range(n + 1)]

    # Zliczanie punktów analogiczne do counting sorta
    for i in range(n):
        G[P[i][0]] += 1
        T[P[i][1]] += 1

    for i in range(n - 1, -1, -1):
        T[i] += T[i + 1]
        G[i] += G[i + 1]

    # Niech każdego i z przedziału [1, ..., n) P[i] = (x, y), wtedy
    # zwracane jest maksimum spośród
    # n - G[x] - T[y] + 1 dla każdego i.
    # (plus 1, ponieważ punkt (x, y) jest zaliczany do obu zbiorów)
    return max(len(P) - G[P[i][0]] - T[P[i][1]] + 1 for i in range(n))


runtests(dominance, all_tests=True)

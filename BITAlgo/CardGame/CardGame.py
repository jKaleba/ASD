from zad5ktesty import runtests


# f(i, j) -> maksymalne wartosci jakie mogą uzyskać gracze
# jeśli grają na przedziale [i, j] -> ***
# funkcja zwraca krotkę (max1, max2),
# gdzie max1 - maksymalna wartość jaką może uzyskać gracz wykonujący ruch,
#       max2 - maksymalna wartość jaką może uzyskać gracz następny

# *** -> po wykonaniu ruchu gracza = wybraniu karty z lewej lub prawej strony,
# drugi gracz będzie wykonywał dokładnie to samo na przedziale
# ograniczonym do [i + 1, j] lub [i, j - 1], odpowiednio do strony wybranej
# poprzednio karty.

# Złożoność czasowa: O(n^2)
# Złożoność pamięciowa: O(n^2)

def garek(A):
    n = len(A)

    # f function
    f = [[(0, 0) for _ in range(n)] for _ in range(n)]

    # Edge cases
    for i in range(n):
        f[i][i] = (A[i], 0)

    for i in range(n - 1):
        f[i][i + 1] = (max(A[i], A[i + 1]), min(A[i], A[i + 1]))

    # General case
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):

            if A[i] + f[i + 1][j][1] > A[j] + f[i][j - 1][1]:
                f[i][j] = (A[i] + f[i + 1][j][1], f[i + 1][j][0])

            else:
                f[i][j] = (A[j] + f[i][j - 1][1], f[i][j - 1][0])

    return f[0][n - 1][0]


runtests(garek)

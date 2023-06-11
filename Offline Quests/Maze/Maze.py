# Jan Kalęba

# Algorytm polega na stworzeniu trzech funkcji,
# f, g, r - oraz odpowiadających im tablic
# F, G, R.
# F - liczy kroki w dół
# G - liczy kroki w górę
# R - wybiera maximum spośród F i G

# Zarówno funkcja F jak i G działa na zasadzie
# weryfikacji, czy w dane miejsce jest w ogóle możliwy
# ruch sprawdzając, czy po 1 - komnata nie jest zamknięta,
# a po drugie, czy z komnaty na lewo lub odpowiednio
# na górze / dole da się do niej dojść - tzn, czy wartość
# na którejś z nich jest różna od -1.
# Jeśli ruch jest możliwy, na dane miejsce w każdej funkcji
# jest wpisywana max wartość z odpowiednich dla niej sąsiadów
# tj. lewo i góra dla F, lewo i dół dla G.

# Finalnie w R[n-1][n-1] będzie znajdować się wartość najdłuższej
# możliwej drogi.


from zad7testy import runtests


def maze(L):
    n = len(L)

    # function for counting down
    F = [[-1 for _ in range(n)] for __ in range(n)]

    # function for counting up
    G = [[-1 for _ in range(n)] for __ in range(n)]

    # Result - function choosing max of F and G
    R = [[-1 for _ in range(n)] for __ in range(n)]

    for row in range(n):
        if L[row][0] == '#':
            break

        F[row][0] = row
        G[row][0] = row
        R[row][0] = row

    for col in range(1, n):
        for row in range(n):
            if L[row][col] != '#' and F[row][col - 1] != -1:
                F[row][col] = F[row][col - 1] + 1
            else:
                # Furthest move impossible
                break

        for row in range(n - 1, -1, -1):
            if L[row][col] != '#' and G[row][col - 1] != -1:
                G[row][col] = G[row][col - 1] + 1
            else:
                # Furthest move impossible
                break

        # Edges
        if L[0][col] != '#' and F[0][col - 1] != -1:
            F[0][col] = F[0][col - 1] + 1
        if L[n - 1][col] != '#' and G[n - 1][col - 1] != -1:
            G[n - 1][col] = G[n - 1][col - 1] + 1

        for row in range(1, n):
            if L[row][col] != '#':
                F[row][col] = max(F[row][col - 1], F[row - 1][col]) + 1
                if F[row][col] == 0:
                    # Move not available
                    F[row][col] -= 1

        for row in range(n - 2, -1, -1):
            if L[row][col] != '#':
                G[row][col] = max(G[row][col - 1], G[row + 1][col]) + 1
                if G[row][col] == 0:
                    # Move not available
                    G[row][col] -= 1

        for row in range(n):
            # Maximum value between F and G
            R[row][col] = max(F[row][col], G[row][col])

        for row in range(n):
            F[row][col] = R[row][col]
            G[row][col] = R[row][col]

    return R[n - 1][n - 1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)

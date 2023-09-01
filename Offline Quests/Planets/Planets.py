from egz1btesty import runtests

from math import inf


# O(n * E^2)
def planetsnE2(D, C, T, E):
    n = len(D)

    # f(i, b) - minimal cost of getting into planet i with b tons of fuel left

    f = [[inf for _ in range(E + 1)] for _ in range(n)]

    teleSource = [False for _ in range(n)]
    teleDestination = [False for _ in range(n)]

    for i in range(n):
        if T[i][0] != i:
            teleSource[i] = True
            teleDestination[T[i][0]] = True

    # Edge case -> first planet with 0 tons of fuel left = 0 cost
    f[0][0] = 0
    # Checking if there is a teleport on the first planet
    if T[0][0] != 0:
        f[T[0][0]][0] = T[0][1]

    for i in range(1, n):
        distance = D[i] - D[i - 1]

        for b in range(E + 1):
            if b + distance <= E:
                for j in range(b + distance + 1):
                    f[i][b] = min(f[i][b],
                                  # way to get to planet i - 1 from planet i with b tons of fuel left
                                  f[i - 1][j] + (b + distance - j) * C[i - 1])

        if teleSource[i]:
            f[T[i][0]][0] = min(f[i][0] + T[i][1], f[T[i][0]][0])

    return min(f[n - 1][b] for b in range(E + 1))


# O(n * E)
def planetsnE(D, C, T, E):
    n = len(D)

    # f(i, b) - minimal cost of being into planet i with b tons of fuel left
    # being != getting there already with b tons left

    f = [[inf for _ in range(E + 1)] for _ in range(n)]

    # sources of teleports
    teleSource = [False for _ in range(n)]

    for i in range(n):
        if T[i][0] != i:
            teleSource[i] = True

    # edge case -> first planet
    for b in range(E + 1):
        f[0][b] = b * C[0]

    # checking if teleport at first planet exists
    if teleSource[0]:
        f[T[0][0]][0] = T[0][1]
        
    # general case
    for i in range(1, n):
        distance = D[i] - D[i - 1]

        # minimum between teleport and getting there by spaceship
        f[i][0] = min(f[i][0], f[i - 1][distance])

        for b in range(1, E + 1 - distance):
            f[i][b] = f[i - 1][b + distance]

        for b in range(1, E + 1):
            f[i][b] = min(f[i][b], f[i][b - 1] + C[i])

        if teleSource[i]:
            f[T[i][0]][0] = min(f[T[i][0]][0], f[i][0] + T[i][1])

    return min(f[n - 1][b] for b in range(E + 1))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planetsnE, all_tests=True)

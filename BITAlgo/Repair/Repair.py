from zad8ktesty import runtests


# Edit Distance | DP Problem

def napraw(s, t):
    n = len(t)
    m = len(s)

    # f(i, j) - liczba zmian potrzebnych do tego, aby z s[0:j + 1] było t[0:i + 1]
    # ([0:k] pomija znak pod k-tym indeksem, stąd + 1)

    #     | e | x | a | m | p | l | e | S |
    # - - - - - - - - - - - - - - - - - - -
    # | e |
    # - - -
    # | g |              ...
    # - - -
    # | T |
    # - - -

    f = [[0 for _ in range(m)] for __ in range(n)]

    # Edge cases

    # (0, 0)
    foundFirst = False
    if s[0] == t[0]:
        foundFirst = True
        f[0][0] = 0
    else:
        f[0][0] = 1

    # First row
    found = foundFirst
    for i in range(1, m):
        substitutionCost = 0
        if s[i] != t[0] or found:
            substitutionCost = 1
        else:
            found = True
        f[0][i] = f[0][i - 1] + substitutionCost

    found = foundFirst
    if s[0] == t[0]:
        found = True

    # First column
    for i in range(1, n):
        substitutionCost = 0
        if t[i] != s[0] or found:
            substitutionCost = 1
        else:
            found = True
        f[i][0] = f[i - 1][0] + substitutionCost

    # General case
    for i in range(1, n):
        for j in range(1, m):
            substitutionCost = 0
            if t[i] != s[j]:
                substitutionCost = 1

            f[i][j] = min(f[i - 1][j - 1] + substitutionCost,
                          f[i - 1][j] + 1,
                          f[i][j - 1] + 1)

    return f[n - 1][m - 1]


runtests(napraw)

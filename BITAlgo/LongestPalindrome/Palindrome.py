from zad2ktesty import runtests


def palindrom2(S):
    # Tutaj proszę wpisać własną implementację
    n = len(S)
    F = [[0 for __ in range(n)] for _ in range(n)]
    for i in range(n):
        F[i][i] = 1

    for i in range(1, n):
        for j in range(0, n - i):
            if (j + 1 > i + j - 1 or F[j + 1][i + j - 1] > 0) and S[i + j] == S[j]:
                F[j][i + j] = i + 1


def palindrom(S):
    n = len(S)

    # f(i, j) - dlugosc najdluzszego podciagu palindromowego o dlugosci i zaczynajacego sie na pozycji j

    f = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        f[i][i] = 1

    maxPali = ""
    maxLen = 0
    for i in range(1, n):
        # i -> length of substring
        for j in range(0, n - i):
            # j -> start of substring

            if S[i + j] == S[j] and (i < 2 or f[j + 1][i + j - 1] > 0):
                f[j][i + j] = i + 1

                if i + 1 > maxLen:
                    maxLen = i + 1
                    maxPali = S[j:i + j + 1]

    return maxPali


runtests(palindrom)

from zad12ktesty import runtests


def sumArr(T, i, j):
    currSum = 0
    for i in range(i, j + 1):
        currSum += T[i]

    return currSum


def autostrada(T, K):
    N = len(T)

    f = [[0 for _ in range(N + 1)] for _ in range(K + 1)]

    # k = 1
    for n in range(1, N + 1):
        f[1][n] = sumArr(T, 0, n - 1)

    # n = 1
    for k in range(1, K + 1):
        f[k][1] = T[0]

    # 2 to k partitions

    for k in range(2, K + 1):
        # 2 to n highways
        for n in range(2, N + 1):
            best = float("inf")
            for x in range(1, n):
                best = min(best, max(f[k - 1][x], sumArr(T, x, n - 1)))
            f[k][n] = best

    return f[K][N]


runtests(autostrada, all_tests=True)

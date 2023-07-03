def subsequence(A: list[int], B: list[int]):
    n = len(A)
    m = len(B)

#   f(i, j) -> longest common subsequence ending at A[i] and B[j]
    f = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                f[i][j] = f[i - 1][j - 1] + 1
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])

    return f[n][m]


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    B = [1, 3, 5, 7, 9]

    print(subsequence(A, B))

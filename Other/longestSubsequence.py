# f(i) - longest subsequence ending at A[i]
# f(i) = max(f(j) + 1) for all j < i and A[j] < A[i]

def longestSubsequence(A: list[int]):
    n = len(A)
    f = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i]:
                f[i] = max(f[i], f[j] + 1)

    return max(f)


if __name__ == '__main__':
    A = [2, 1, 4, 3, 1, 5, 2, 7, 8, 3]

    print(longestSubsequence(A))

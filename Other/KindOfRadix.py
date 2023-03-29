from random import randint


# array with length = n
# contains values
# [0, n^2)
# sort in linear time

def radixForNumbers(A):
    n = len(A)
    B = [0 for _ in range(n)]
    C = [0 for _ in range(n)]

    for i in range(n):
        C[A[i] % n] += 1

    for i in range(1, n):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[A[i] % n] -= 1
        B[C[A[i] % n]] = A[i]

    for i in range(n):
        A[i] = C[i] = 0

    for i in range(n):
        C[B[i] // n] += 1

    for i in range(1, n):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[B[i] // n] -= 1
        A[C[B[i] // n]] = B[i]


if __name__ == '__main__':
    N = 100
    T = [randint(0, N * N - 1) for _ in range(N)]
    print(T)
    radixForNumbers(T)
    print(T)

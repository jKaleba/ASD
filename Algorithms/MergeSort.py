import random


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def merge(A, l, m, r):

    n1 = m - l + 1
    n2 = r - m

    L = [None for _ in range(n1)]
    R = [None for _ in range(n2)]

    for i in range(n1):
        L[i] = A[l + i]
    for j in range(n2):
        R[j] = A[m + j + 1]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

def mergeSort(A, l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(A, l, m)
        mergeSort(A, m + 1, r)

        merge(A, l, m, r)


if __name__ == '__main__':
    S = [random.randint(0, 100) for _ in range(100)]
    n = len(S)
    mergeSort(S, 0, n - 1)
    print(S)
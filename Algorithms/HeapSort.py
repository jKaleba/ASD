import random


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def maxHeapify(A, i, n):

    l = left(i)
    r = right(i)

    max_ind = i
    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r

    if max_ind != i:
        swap(A, i, max_ind)
        maxHeapify(A, max_ind, n)


def buildHeap(A):
    n = len(A)

    for i in range(parent(n - 1), -1, -1):
        maxHeapify(A, i, n)



def heapSort(A):
    n = len(A)

    buildHeap(A)

    for i in range(n - 1, 0, -1):
        swap(A, 0, i)
        maxHeapify(A, 0, i)



if __name__ == '__main__':
    S = [random.randint(0, 100) for i in range(100)]
    heapSort(S)
    print(S)
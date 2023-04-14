import random


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def bubbleSort(A):
    n = len(A)
    for i in range(n):
        for j in range(1, n - i):
            if A[j] < A[j - 1]:
                swap(A, j, j - 1)

def combSort(A):
    n = len(A)
    gap = n
    shrink = 1.5
    swapped = True

    while gap > 1 or swapped:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1

        i = 0
        swapped = False
        while i + gap < n:
            if A[i] > A[i + gap]:
                swap(A, i, i + gap)
                swapped = True
            i += 1

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            swap(A, j, j - 1)
            j -= 1

def selectionSort(A):
    n = len(A)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if A[j] < A[min_idx]:
                min_idx = i
        swap(A, i, min_idx)


if __name__ == '__main__':
    S = [random.randint(0, 100) for _ in range(3000)]
    insertionSort(S)
    print(S)
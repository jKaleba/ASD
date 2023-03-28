# k-chaotic array
#      <=>
# every element is on its
# after-sort-place within
# accuracy reaching no more
# than k.

# nlogk complexity
# n = len(array)
# k = size of heap
#       =
# parameter of k-chaotic array

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def parent(i):
    return (i - 1) // 2

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def minHeapify(A, i, k, n):
    l = left(k)
    r = right(k)

    min_idx = k
    if l < n and A[i + l] < A[i + min_idx]:
        min_idx = l
    if r < n and A[i + r] < A[i + min_idx]:
        min_idx = r

    if min_idx != k:
        swap(A, i + k, i + min_idx)
        minHeapify(A, i, min_idx, n)

def buildMinHeap(A, k):
    for i in range(parent(k - 1), -1, -1):
        minHeapify(A, 0, i, k)

def shuffle(A, k):
    # TODO
    # function irrelevant from the point of
    # this task, but in order to see entirety
    # in full action, should be done

    # primitive shuffling each next k elements
    # with each other
    n = len(A)
    for j in range(0, n, k):

        x = min(k - 1, n - j - 1)
        temp = A[j]
        for s in range(x):
            A[j + s] = A[j + s + 1]
        A[j + x] = temp

if __name__ == '__main__':

    T = [i for i in range(30)]
    K = 3
    N = len(T)
    T = sorted(T)
    shuffle(T, K)
    print(T)

    buildMinHeap(T, K)

    for i in range(N):
        minHeapify(T, i, 0, min(K, N - i))

    print(T)
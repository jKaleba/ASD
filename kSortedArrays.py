from random import randint


# k sorted arrays of the same size
# N elements in entirety
# sort it in O(Nlogk) complexity


def heapSort(T):
    # FUNCTIONS #
    def left(i):
        return 2 * i + 1

    def right(i):
        return 2 * i + 2

    def parent(i):
        return (i - 1) // 2

    def swap(A, i, j):
        A[i], A[j] = A[j], A[i]

    def buildHeap(A):
        n = len(A)

        for i in range(parent(n - 1), -1, -1):
            minHeapify(A, i, n)

    def minHeapify(A, i, n):
        l = left(i)
        r = right(i)

        min_idx = i
        if l < n and A[l][0] < A[min_idx][0]:
            min_idx = l
        if r < n and A[r][0] < A[min_idx][0]:
            min_idx = r

        if min_idx != i:
            swap(A, i, min_idx)
            minHeapify(A, min_idx, n)

    ##########
    k = len(T)
    N = k * len(T[0])
    h = [(T[i][0], i) for i in range(k)]
    idx = [0 for _ in range(k)]
    f = len(T[0])

    buildHeap(h)
    res = [None for _ in range(N)]
    for i in range(N):
        res[i] = h[0][0]

        idx[h[0][1]] += 1
        if idx[h[0][1]] < f:
            h[0] = (T[h[0][1]][idx[h[0][1]]], h[0][1])
        #            |  row  |    column   |    row   |
        else:
            k -= 1
            h[0] = h[k]

        minHeapify(h, 0, k)

    return res

def sortNaturalSeries(A):
    # FUNCTIONS #
    def merge(L1, L2):
        n = len(L1)
        m = len(L2)
        res = [None for _ in range(n + m)]

        i = j = 0
        while i < n and j < m:
            if L1[i] <= L2[j]:
                res[i + j] = L1[i]
                i += 1
            else:
                res[i + j] = L2[j]
                j += 1

        while i < n:
            res[i + j] = L1[i]
            i += 1
        while j < m:
            res[i + j] = L2[j]
            j += 1

        return res

    def concat(L2):
        A[(out + length) % buffSize] = L2

    def done():
        return length == 1

    def getNatSer(idx):
        return A[idx]

    ##########
    buffSize = len(A)
    out = 0
    length = len(A)
    while not done():

        l1 = getNatSer(out);    out = (out + 1) % buffSize;   length -= 1
        l2 = getNatSer(out);    out = (out + 1) % buffSize;   length -= 1

        new = merge(l1, l2)
        concat(new);            length += 1

    return A[out]

if __name__ == '__main__':

    mRange = (0, 50)
    height = randint(10, 15)
    width = randint(10, 15)

    X = [sorted([randint(*mRange) for _ in range(width)]) for __ in range(height)]

    linearX = heapSort(X)
    print(linearX)
    print(len(linearX))

    linearX = sortNaturalSeries(X)
    print(linearX)
    print(len(linearX))

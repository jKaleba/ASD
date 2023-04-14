from random import randint

# Statystyki pozycyjne -->
# k-ta statystyka pozycyjna
#           =
# element tablicy A, który znajdowałby
# się na k-tej pozycji po posortowaniu


# Zwykły select ma złożoność O(n),
# ale w przypadku pechowych danych
# może się ukwadratowić
def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def partition(A, p, r):
    idx = randint(p, r)
    swap(A, idx, r)
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            swap(A, i, j)

    swap(A, i + 1, r)
    return i + 1

def select(A, k):
    p, r = 0, len(A) - 1
    while p < r:
        q = partition(A, p, r)
        if q == k:
            return A[k]
        elif q > k:
            r = q - 1
        elif q < k:
            p = q + 1

    return A[k]


# Magiczne piątki zapewniają, że
# select zawsze wykona się w czasie
# liniowym.
def pivot(A):
    n = len(A)
    if len(A) == 1:
        return A[0]

    M = [[A[i + j] for i in range(min(5, n - j))] for j in range(0, n, 5)]

    m = [select(M[i], 5 // 2) for i in range(n)]
    return pivot(m)

def magicPartition(A, p, r):
#       FIXME
    idx = pivot(A)
    swap(A, idx, r)
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            swap(A, i, j)

    swap(A, i + 1, r)
    return i + 1

def magicFives(A, k):
    p, r = 0, len(A) - 1
    while p < r:
        q = magicPartition(A, p, r)
#       FIXME
        if q == k:
            return A[k]
        elif q > k:
            r = q - 1
        elif q < k:
            p = q + 1

    return A[k]

if __name__ == '__main__':
    mRange = 100
    T = [(randint(0, 100)) for i in range(mRange)]
    print(T)

    print(select(T, len(T) // 2))
    print(magicFives(T, len(T) // 2))

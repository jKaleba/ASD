from kol1testy import runtests


# Jan Kalęba

# Algorytm polega na przechodzeniu po tablicy
# tworząc kopię aktualnych p elementów,
# spośród których za pomocą funkcji select
# znajdowana jest k-ta największa wartość wśród
# indeksow i, i + p.
# Select domyślnie znajduje liczbę na k-tej pozycji,
# czyli k-tą najmniejszą, więc do funkcji
# przekazywane jest p - k, co równoznaczne jest
# szukaniu k-tej największej
# Po znalezieniu, liczba dodawana jest do aktualnej sumy.


# Złożoność czasowa O(np)
# Złożoność pamięciowa O(np) -> n razy slicing - niby jest garbage collector,
#                                                ale nie jest brany pod uwagę


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def partition(A, p, r):
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


def ksum(T, k, p):
    n = len(T)
    sum = 0

    for i in range(n - p + 1):
        X = T[i: i + p]
        y = select(X, p - k)  # -> O(p)
        sum += y

    return sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=True)

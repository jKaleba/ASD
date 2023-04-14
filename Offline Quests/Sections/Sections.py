from zad2testy import runtests
from random import randint


# Algorytm sortuje tablicę przedziałów względem końca
# każdego z nich.
# Następnie po kolei sprawdza, ile przedziałów kończy się na lewo
# na osi oX względem aktualnego, sortuje względem początków,
# po czym sprawdza dla nich analogiczną sytuację.

# O(nlogn)


def swap(A, i, j, B=None):
    A[i], A[j] = A[j], A[i]

    if B is not None:
        B[i], B[j] = B[j], B[i]


def partition(A, p, r, parameter, B=None):
    swap(A, randint(p, r), r, B)

    x = A[r][parameter]
    i = p - 1

    for j in range(p, r):
        if A[j][parameter] <= x:
            i += 1
            swap(A, i, j, B)

    swap(A, i + 1, r, B)
    return i + 1


def quickSort(A, p, r, parameter, B=None):
    if p < r:
        q = partition(A, p, r, parameter, B)
        quickSort(A, p, q - 1, parameter, B)
        quickSort(A, q + 1, r, parameter, B)


# F - zwraca tablicę zawierającą liczniki
# dla każdego przedziału, ile innych kończy się
# na lewo lub w tym samym miejscu względem osi oX.
def F(L):
    n = len(L)
    quickSort(L, 0, n - 1, 1)
    f = [0 for _ in range(n)]

    f[n - 1] = n - 1
    for i in range(n - 2, -1, -1):
        if L[i][1] == L[i + 1][1]:
            f[i] = f[i + 1]
        else:
            f[i] = i

    return f


# G - zwraca tablicę zawierającą liczniki
# dla każdego przedziału, ile innych zaczyna się
# na lewo względem osi oX.
# Przed zliczeniem sortuje jednocześnie tablicę
# przedziałów L i tablicę funkcji F,
# co następnie umożliwia porównanie ze sobą
# wartości funkcji F i G dla każdego przedziału,
# i wybrać ten zawierający najwięcej pozostałych
# w czasie liniowym.
def G(L, f):
    n = len(L)
    quickSort(L, 0, n - 1, 0, f)

    g = [0 for _ in range(n)]

    g[0] = 0
    for i in range(1, n):
        if L[i][0] == L[i - 1][0]:
            g[i] = g[i - 1]
        else:
            g[i] = i
    return g


def depth(L):
    N = len(L)
    maxInside = 0

    f = F(L)
    g = G(L, f)

    i = 0
    limit = N
    while i < limit:
        curr = f[i] - g[i]
        if curr > maxInside:
            maxInside = curr
            limit = N - maxInside

        i += 1

    return maxInside


runtests(depth)

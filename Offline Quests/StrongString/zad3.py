import random

from zad3testy import runtests


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def partition(A, p, r):

    idx = random.randint(p, r)
    swap(A, idx, r)

    x = A[r]

    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            swap(A, i, j)

    swap(A, i + 1, r)
    return i + 1


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)


def czolg(A):
    n = len(A)
    maxC = 0
    for i in range(n - 1):
        c = 1
        for j in range(i + 1, n):
            if A[i] == A[j] or A[i] == A[j][::-1]:
                c += 1
        if c > maxC:
            maxC = c

    return maxC


def palindrome(word):
    n = len(word)
    for i in range(n // 2):
        if word[i] != word[n - i - 1]:
            return False

    return True

def strong_string(T):
    n = len(T)

    # O(N)
    for i in range(n):
        if not palindrome(T[i]):
            T.append(T[i][::-1])


    n = len(T)
    # O(nlogn)
    quickSort(T, 0, n - 1)

    # O(n)
    maxStrength = 1
    currStrength = 1
    for i in range(1, n):
        if T[i] == T[i - 1]:
            currStrength += 1

        else:
            if currStrength > maxStrength:
                maxStrength = currStrength
            currStrength = 1

    if currStrength > maxStrength:
        maxStrength = currStrength

    return maxStrength



# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )

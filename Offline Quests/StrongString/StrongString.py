from zad3testy import runtests
from random import randint


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


def palindrome(word):
    n = len(word)

    for i in range(n // 2):
        if word[i] != word[n - i - 1]:
            return False

    return True


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)


def strong_string(T):
    n = len(T)
    maxLen = 0

    for i in range(1, n):
        if len(T[i]) > maxLen:
            maxLen = len(T[i])

    buckets = [[] for _ in range(maxLen)]
    for i in range(n):
        buckets[len(T[i]) - 1].append(T[i])
        if not palindrome(T[i]):
            buckets[len(T[i]) - 1].append(T[i][::-1])

    maxStrength = 1
    for i in range(maxLen):
        currStr = 1

        quickSort(buckets[i], 0, len(buckets[i]) - 1)
        for j in range(1, len(buckets[i])):
            if buckets[i][j] == buckets[i][j - 1]:
                currStr += 1
            else:
                if currStr > maxStrength:
                    maxStrength = currStr
                if len(buckets[i]) - j < maxStrength:
                    break

                currStr = 1

        if currStr > maxStrength:
            maxStrength = currStr

    return maxStrength


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests(strong_string, all_tests=True)

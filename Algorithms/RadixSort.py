import random


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def countingSort(A, idx):
    n = len(A)
    k = 26

    C = [0 for _ in range(k)]
    B = [None for _ in range(n)]
    
    for i in range(n):
        C[ord(A[i][idx]) - ord("a")] += 1

    for i in range(1, k):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[ord(A[i][idx]) - ord("a")] -= 1
        B[C[ord(A[i][idx]) - ord("a")]] = A[i]

    for i in range(n):
        A[i] = B[i]

def radixSort(A):
    wordsLen = len(A[0])
    for idx in range(wordsLen - 1, -1, -1):
        countingSort(A, idx)


if __name__ == '__main__':
    words = 100
    t = 100

    Arr = []
    for x in range(words):
        str = ""
        for j in range(t):
            str += chr(random.randint(97, 122))

        Arr.append(str)

    radixSort(Arr)
    for word in Arr:
        print(word)
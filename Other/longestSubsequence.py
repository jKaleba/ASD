# f(i) - longest subsequence ending at A[i]
# f(i) = max(f(j) + 1) for all j < i and A[j] < A[i]

def longestSubsequenceN2(A: list[int]):
    n = len(A)
    f = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i]:
                f[i] = max(f[i], f[j] + 1)

    return max(f)


def longestSubsequenceNlogN(A: list[int]):
    def findSmallestBiggerElement(B: list[int], l, r, value):
        while l < r:
            mid = (l + r) // 2
            if B[mid] < value:
                l = mid + 1
            else:
                r = mid

        return l

    ########################################################

    n = len(A)
    sequence = [A[0]]
    for i in range(1, n):
        idx = findSmallestBiggerElement(sequence, 0, len(sequence), A[i])
        if idx == len(sequence):
            sequence.append(A[i])
        else:
            sequence[idx] = A[i]

    return len(sequence)


if __name__ == '__main__':
    from random import randint
    for i in range(1000):
        A = [randint(1, 100) for _ in range(randint(1, 150))]
        if longestSubsequenceN2(A) != longestSubsequenceNlogN(A):
            print("Wrong answer")

    else:
        print("Passed all tests.")

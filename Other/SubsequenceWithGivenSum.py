from Knapsack import knapsack


def subsequence(A: list[int], value):
    B = [A[i] for i in range(10)]
    if knapsack(A, B, value) == value:
        return True

    return False


if __name__ == '__main__':
    A = [5, 2, 3, 2, 2, 5, 1, 3, 3, 8]
    val = 24

    print(A)
    print(val)
    print(subsequence(A, val))

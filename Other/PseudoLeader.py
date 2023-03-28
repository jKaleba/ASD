from random import randint

# Pseudolider -> element w tablicy
# jest pseudoliderem <=> gdy zajmuje
# ponad 1/3 jej indeksów.

def shuffle(A):
    n = len(A)
    for i in range(n - 1):
        k = randint(0, n - 1)
        A[i], A[k] = A[k], A[i]

def pseudoLeader(A):
    # O(n)

    n = len(A)
    candidates = [A[0], A[1]]
    counters = [1, 1]
    i = 2

    while i != n:
        if A[i] == candidates[0]:
            counters[0] += 1
        elif A[i] == candidates[1]:
            counters[1] += 1
        elif counters[0] == 0:
            candidates[0] = A[i]
            counters[0] = 1
        elif counters[1] == 0:
            candidates[1] = A[i]
            counters[1] = 1
        else:
            counters[0] -= 1
            counters[1] -= 1

        i += 1

    counters = [0, 0]
    for i in range(n):
        if A[i] == candidates[0]:
            counters[0] += 1
        elif A[i] == candidates[1]:
            counters[1] += 1

    result = []
    print(candidates)
    if counters[0] > n // 3:
        result.append(candidates[0])
    if counters[1] > n // 3:
        result.append(candidates[1])

    return result

if __name__ == '__main__':

    T = []
    size = randint(10, 20)
    l = size // 3 + 1
    l1Value = randint(0, 20)
    l2Value = randint(0, 20)
    print("Size:", size, "l:", l, "l1Val:", l1Value, "l2Val:", l2Value)

    for j in range(l):
        T.append(l1Value)
    for j in range(l):
        T.append(l2Value)
    for j in range(2 * l, size):
        T.append(randint(0, 20))
    shuffle(T)

    print(T)
    print(pseudoLeader(T))


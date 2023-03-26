from random import randint

# Lider -> element w tablicy
# jest liderem <=> gdy zajmuje
# ponad jej połowę.

def shuffle(A):
    n = len(A)
    for i in range(n - 1):
        k = randint(0, n - 1)
        A[i], A[k] = A[k], A[i]

def leader(A):
    # O(n)

    n = len(A)
    currLead = A[0]
    i = counter = 1

    while i != n:
        if A[i] == currLead:
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            currLead = A[i]

        i += 1

    counter = 0
    for i in range(n):
        if A[i] == currLead:
            counter += 1

    print(n, counter)
    if counter > n // 2:
        return currLead
    return -1

if __name__ == '__main__':

    T = []
    size = randint(10, 20)
    l = randint(size // 2 - size // 10, size // 2 + size // 5)
    lValue = randint(0, 20)
    print("Size:", size, "l:", l, "lVal:", lValue)

    for j in range(l):
        T.append(lValue)
    for j in range(l, size):
        T.append(randint(0, 20))
    shuffle(T)

    print(T)
    print(leader(T))


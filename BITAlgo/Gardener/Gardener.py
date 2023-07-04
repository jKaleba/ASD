from zad7ktesty import runtests

from Other.Knapsack import knapsack
from queue import Queue


# Solved using Knapsack algorithm
# *******************************
# Weights = liters required for each root
# Prices = profit from each tree - Z array
# Capacity = l - liters of water

def cost(T, D):
    n = len(T)
    m = len(T[0])
    visited = [[False for j in range(m)] for i in range(n)]

    A = [1, -1, 0, 0]
    B = [0, 0, 1, -1]

    result = [0 for _ in range(len(D))]

    for idx, coord in enumerate(D):

        currCost = 0

        Stack = Queue()
        Stack.put((0, coord))
        visited[0][coord] = True

        while not Stack.empty():
            i, j = Stack.get()

            currCost += T[i][j]

            for k in range(len(A)):
                x = i + A[k]
                y = j + B[k]

                if 0 <= x < n and 0 <= y < m and not visited[x][y] and T[x][y] != 0:
                    Stack.put((x, y))
                    visited[x][y] = True

        result[idx] = currCost

    return result


def ogrodnik(T, D, Z, l):

    res = cost(T, D)
    return knapsack(res, Z, l)


runtests(ogrodnik, all_tests=True)

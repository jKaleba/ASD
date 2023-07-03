# Knapsack problem

def knapsack(W, P, B):
    n = len(W)
    F = [[0 for b in range(B + 1)] for i in range(n)]

    for b in range(W[0], B + 1):
        F[0][b] = P[0]

    for b in range(B + 1):
        for i in range(1, n):
            F[i][b] = F[i - 1][b]
            if b - W[i] >= 0:
                F[i][b] = max(F[i][b], F[i - 1][b - W[i]] + P[i])

    return F[n - 1][B]


if __name__ == '__main__':
    Weight = [2, 3, 4, 5]
    Prices = [3, 4, 5, 6]
    maxWeight = 8

    print(knapsack(Weight, Prices, maxWeight))

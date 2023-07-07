from zad9ktesty import runtests


def F(P, H, idx, G, D, cars):
    n = len(P)

    carIdx = n - idx - 1

    if idx == 0 and P[carIdx] <= min(G, D):
        cars[carIdx] = "B"  # both
        H[idx][G][D] = 1

    else:
        if P[carIdx] <= min(G, D):
            x = F(P, H, idx - 1, G - P[carIdx], D, cars) + 1
            y = F(P, H, idx - 1, G, D - P[carIdx], cars) + 1

            if x > y:
                cars[carIdx] = "G"
            else:
                cars[carIdx] = "D"
            H[idx][G][D] = max(x, y)

        elif P[carIdx] <= G:
            H[idx][G][D] = F(P, H, idx - 1, G - P[carIdx], D, cars) + 1
            cars[carIdx] = "G"
        elif P[carIdx] <= D:
            H[idx][G][D] = F(P, H, idx - 1, G, D - P[carIdx], cars) + 1
            cars[carIdx] = "D"

    return H[idx][G][D]


# Error w testach, mimo poprawnego podziału i poprawnego maksymalnego wyniku,
# jak również poprawnego ostatniego elementu w podziałach.
def prom(P, G, D):
    n = len(P)

    # f(i, G, D) - maksymalna liczba samochodów z przedziału {0, ..., i},
    # które można umieścić na platformach G i D

    f = [[[0 for _ in range(D + 1)] for __ in range(G + 1)] for ___ in range(n)]
    cars = [None for _ in range(n)]
    v = F(P, f, n - 1, G, D, cars)

    platforms = [[] for _ in range(2)]
    lastLetter = cars[v - 1]
    for i in range(v):
        if cars[i] == lastLetter:
            platforms[0].append(i)
        else:
            platforms[1].append(i)

    return platforms[0]


runtests(prom)

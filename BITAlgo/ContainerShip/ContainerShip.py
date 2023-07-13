from zad11ktesty import runtests


def kontenerowiec(T):
    n = len(T)
    S = sum(T)

    # g(i, j) -> czy na korzystając z i przedmiotów można na jednej
    # połowie statku uzyskać ciężar j -> druga połowa wyliczana za pomocą S - j
    g = [[False for _ in range(S + 1)] for _ in range(n)]

    # Edge case -> pierwszy przedmiot
    g[0][T[0]] = True
    for idx in range(1, n):

        for firstHalfWeight in range(S + 1):
            if not g[idx][firstHalfWeight]:
                g[idx][firstHalfWeight] = g[idx - 1][firstHalfWeight]

            if g[idx - 1][firstHalfWeight]:
                g[idx][firstHalfWeight + T[idx]] = True

    minDifference = S
    for firstHalfWeight in range(S + 1):
        secondHalfWeight = S - firstHalfWeight
        if g[n - 1][firstHalfWeight] and abs(secondHalfWeight - firstHalfWeight) < minDifference:
            minDifference = abs(secondHalfWeight - firstHalfWeight)

    return minDifference


runtests(kontenerowiec)

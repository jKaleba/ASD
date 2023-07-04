from zad3ktesty import runtests


# O(nk)
def ksuma(T, k):
    n = len(T)

    # f(i) - najmniejsza suma zawierająca T[i], dla ktorej między dowolnymi elementami nie ma odleglosci <= k
    f = [0 for _ in range(n)]
    for i in range(k):
        f[i] = T[i]

    for i in range(k, n):
        # O(k)
        f[i] = min(f[i - k:i]) + T[i]

    return min(f[n - k:n])


runtests(ksuma)

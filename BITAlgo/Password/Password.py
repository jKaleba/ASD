from zad6ktesty import runtests


def haslo(S):
    n = len(S)

    print(S)

    # f(i) -> liczba sposobów na zaszyfrowanie pierwszych i znaków
    f = [0 for _ in range(n)]

    # Edge cases
    f[0] = 1
    if S[1] != '0':
        f[1] = f[0]
    if S[1] != '0' and int(S[0:2]) <= 26:
        f[1] = 2

    # General case
    for i in range(2, n):
        if S[i] != '0':
            f[i] = f[i - 1]

        if S[i - 1] != '0' and int(S[i - 1:i + 1]) <= 26:
            f[i] += f[i - 2]

    return f[n - 1]


runtests(haslo)

from zad1ktesty import runtests

def roznica(S):
    n = len(S)

    # f(i) - maxymalna roznica w podciagu konczacym sie na i
    f = [0 for _ in range(n)]

    f[0] = 1 if S[0] == '0' else -1

    for i in range(1, n):
        if S[i] == '0':
            f[i] = max(f[i - 1] + 1, 1)
        else:
            f[i] = max(f[i - 1] - 1, -1)

    return max(f)


runtests(roznica)

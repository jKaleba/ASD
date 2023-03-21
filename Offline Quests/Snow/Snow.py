# Jan Kaleba

# Algorytm opiera sie na klasycznym heapsorcie
# jaki był przedstawiony na wykladzie, z ta roznica,
# ze gdy najwiekszy element w kopcu jest mniejszy niz
# ilosc dni w ktorych bedzie zbierany snieg, dalsze sortowanie
# jest przerywane, a ich wartosci nie są dodawane do sumy.
# Patrzac na wartosci sniegu w nieposortowanej tablicy- takiej jak w poleceniu,
# wartosci mniejsze niz ilosc dni potrzebnych do zebrania najwiekszych
# ilosci sniegu sa pomijane przy zbieraniu, poniewaz inaczej prowadziloby
# to za kazdym razem do straty rownej co do wartosci roznicy miedzy iloscia
# elementow wiekszych niz ilosc dni, a zebrana iloscia sniegu.

from zad2testy import runtests

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def parent(i):
    return (i - 1) // 2

def heapify(A, i, n):
    l = left(i)
    r = right(i)

    max_ind = i
    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r

    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, max_ind, n)

def build_heap(A):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        heapify(A, i, n)

def snow( S ):
    n = len(S)
    build_heap(S)
    days = 0
    sum = 0
    for i in range(n - 1, 0, -1):
        if S[0] < days:
            return sum

        sum += S[0] - days
        days += 1
        S[0], S[i] = S[i], S[0]
        heapify(S, 0, i)

    return sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )

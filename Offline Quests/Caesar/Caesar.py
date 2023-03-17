# Jan Kalęba

# Algorytm polega na iterowaniu przez
# indeksy tak długo, aż pozostała liczba indeksów
# będzie mniejsza niż połowa długości najdłuższego aktualnie palindromu,
# ponieważ jakikolwiek palindrom znaleziony w dalszej częsci, na pewno
# nie osiągnie większej długości.
# Dla każdego aktualnie przetwarzanego elementu, najpierw sprawdzany jest warunek,
# czy elementy odległe od niego o długość połowy najdłuższego palindromu są takie same,
# w przeciwnym wypadku nie ma sensu sprawdzać jego długości, gdyż na pewno nie przekroczy
# aktualnie największej.


from zad1testy import runtests

def ceasar( s ):

    index = 1
    mLen = 1
    n = len(s) -  1
    k = len(s)
    l = 1

    while index < n:

        if s[index - l] == s[index + l]:
            currLen = 1
            distance = 1
            while index - distance >= 0 and index + distance < k and s[index - distance] == s[index + distance]:
                distance += 1
                currLen += 2

            if currLen > mLen:
                mLen = currLen
                n = len(s) - mLen // 2 - 1
                l = mLen // 2 + 1

        index += 1

    return mLen

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )

from zad4testy import runtests


def students(T, idx):
    return T[idx][0] * (T[idx][2] - T[idx][1])


def collide(T, i, j):
    return not (T[i][2] < T[j][1] or T[i][1] > T[j][2])


def select_buildings(T, p):
    n = len(T)

    # f(i, b) - max students for buildings between 0 and i (including i)
    # with b budget

    F = [[0 for b in range(p + 1)] for i in range(n)]

    # T[i] = (height, left, right, cost)
    # T2 -> storing objects with its original indices -> (T[i], i)
    T2 = [(T[i], i) for i in range(n)]
    # Sorting by height
    T2.sort(key=lambda x: x[0][2])
    T.sort(key=lambda x: x[2])

    # Vector of original indices
    vector = [idx for (Object, idx) in T2]

    # Filling first row <=> cost of 1st dorm <= budget
    for b in range(T[0][3], p + 1):
        F[0][b] = students(T, 0)

    for b in range(p + 1):
        for i in range(1, n):
            F[i][b] = F[i - 1][b]

            # Checking if we can afford ith dorm
            if b - T[i][3] >= 0:
                for j in range(i - 1, -1, -1):
                    if not collide(T, i, j):
                        F[i][b] = max(F[i][b], F[j][b - T[i][3]] + students(T, i))
                        break

                    else:
                        F[i][b] = max(F[i][b], students(T, i))

    # Traceback
    i = n - 1
    b = p
    result = []

    while i >= 0:
        # General case
        if i != 0 and F[i][b] != F[i - 1][b]:
            # after considering ith building
            after = F[i][b]

            # current dormitory volume - ith dorm
            currentDorm = students(T, i)
            result.append(vector[i])

            b -= T[i][3]
            j = i - 1

            # Finding previous building
            while j >= 0 and F[j][b] + currentDorm != after:
                j -= 1
                i -= 1

        # First building
        elif i == 0 and F[i][b] != 0:
            result.append(vector[i])

        i -= 1

    result.sort()

    return result


runtests(select_buildings)

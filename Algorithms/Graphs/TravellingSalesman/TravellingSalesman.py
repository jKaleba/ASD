import Algorithms.Graphs.FloydWarshall as fw

global N, distances, DP, completed_visit


def tsp(mark, position):
    if mark == completed_visit:
        return distances[position][0]

    if DP[mark][position] != -1:
        return DP[mark][position]

    ans = float('inf')

    for i in range(N):
        if not (mark & (1 << i)):
            ans = min(ans, distances[position][i] + tsp(mark | (1 << i), i))

    DP[mark][position] = ans

    return ans


if __name__ == '__main__':

    file = open("cities.txt", "r", encoding="utf-8")

    N, starting_city = file.readline().strip().split()
    N = int(N)

    lines = file.readlines()

    cities = {line.strip().split()[0] for line in lines}
    cities.add("Rzeszów")

    city_to_idx = {city: idx for (idx, city) in enumerate(cities)}

    graph = [[] for _ in range(N)]

    starting_idx = city_to_idx[starting_city]

    for edge in lines:
        curr_line = edge.strip()
        A, B, distance = curr_line.split()
        distance = int(distance)
        x, y = city_to_idx[A], city_to_idx[B]

        graph[x].append((y, distance))
        graph[y].append((x, distance))

    DP = [[-1 for _ in range(N)] for _ in range(2 ** N)]
    distances = fw.FloydWarshall(graph)
    completed_visit = (1 << N) - 1

    print(tsp(1, 0))

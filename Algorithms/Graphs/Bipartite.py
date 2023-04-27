from collections import deque

UNVISITED = 0
IN_QUEUE = 1
VISITED = 2


def bipartite(Graph: list[list[int]]):
    n = len(Graph)

    Q = deque()
    Q.append(0)

    coloring = [None for _ in range(n)]
    state = [UNVISITED for _ in range(n)]
    state[0] = IN_QUEUE
    coloring[0] = True

    while len(Q) != 0:
        vertex = Q.popleft()

        for u in Graph[vertex]:
            if state[u] == UNVISITED:
                coloring[u] = not coloring[vertex]
                Q.append(u)
                state[u] = IN_QUEUE
            else:
                if coloring[u] == coloring[vertex]:
                    return False
        state[vertex] = VISITED

    return True


if __name__ == '__main__':

    num_nodes = 8
    partition_size = 4
    graph = [[] for _ in range(num_nodes)]

    # Add edges between the two partitions
    for i in range(partition_size):
        for j in range(partition_size, num_nodes):
            # Add an edge between node i in the first partition
            # and node j in the second partition
            graph[i].append(j)
            graph[j].append(i)

    # Print the adjacency list representation of the graph
    for i in range(num_nodes):
        print(f"Node {i}: {graph[i]}")

    print(f"Bipartite: {bipartite(graph)}")

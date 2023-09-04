class Solution:

    @staticmethod
    def maxEnvelopesN2(envelopes: list[list[int]]) -> int:
        ##########################################
        def topologicalSort(Graph: list[list[int]]):
            m = len(Graph)
            visited = [False for _ in range(m)]
            sortedGraph = [0 for _ in range(m)]
            idx = m - 1

            def DFS(u):
                nonlocal idx

                visited[u] = True
                for v in Graph[u]:
                    if not visited[v]:
                        DFS(v)
                sortedGraph[idx] = u
                idx -= 1

            for i in range(m):
                if not visited[i]:
                    DFS(i)

            return sortedGraph

        def longestPath(Graph: list[list[int]]):
            m = len(Graph)
            sortedGraph = topologicalSort(Graph)
            pathLength = [1 for _ in range(m)]

            for u in sortedGraph:
                for v in Graph[u]:
                    pathLength[v] = max(pathLength[v], pathLength[u] + 1)

            return max(pathLength)

        ##########################################
        n = len(envelopes)

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        depends = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if envelopes[i][0] < envelopes[j][0] and envelopes[i][1] < envelopes[j][1]:
                    depends[i].append(j)

        return longestPath(depends)

    @staticmethod
    def maxEnvelopesNlogN(envelopes: list[list[int]]) -> int:
        ##########################################
        def lesser(A: tuple, B: tuple):
            return A[0] < B[0] and A[1] < B[1]

        def findSmallestBiggerElement(B: list[tuple[int, int]], l: int, r: int, currEnv: tuple):
            while l < r:
                mid = (l + r) // 2
                if lesser(B[mid], currEnv):
                    l = mid + 1
                else:
                    r = mid

            return l

        ##########################################
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        seq = [envelopes[0]]
        for i in range(1, n):
            idx = findSmallestBiggerElement(seq, 0, len(seq), envelopes[i])
            if idx == len(seq):
                seq.append(envelopes[i])

            else:
                seq[idx] = envelopes[i]

        return len(seq)


if __name__ == '__main__':
    test0 = [[5, 4], [6, 4], [6, 7], [2, 3]]
    test1 = [[1, 1], [1, 1], [1, 1]]

    print(Solution.maxEnvelopesN2(test0))
    print(Solution.maxEnvelopesN2(test1))
    print(Solution.maxEnvelopesNlogN(test0))
    print(Solution.maxEnvelopesNlogN(test1))

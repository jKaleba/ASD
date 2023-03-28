from random import randint

# Structure with 3 operations performed
# in O(logn) complexity
# 1. pop min element
# 2. pop max element
# 3. insert

# Solution are two heaps, one maxHeap,
# one minHeap, both storing tuples.
# Both stores the same values
# in tuples with indices of those values
# in other heap.


def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def parent(i):
    return (i - 1) // 2

def swap(A, i, j, B):
    temp = B[A[i][1]][1]
    B[A[i][1]] = (B[A[i][1]][0], B[A[j][1]][1])
    B[A[j][1]] = (B[A[j][1]][0], temp)

    A[i], A[j] = A[j], A[i]


class TwinHeaps:
    length: int
    maxLength = 20
    maxHeap: list
    minHeap: list

    def __init__(self, arr):
        self.length = len(arr)
        self.maxHeap = [None for _ in range(self.maxLength)]
        self.minHeap = [None for _ in range(self.maxLength)]

        for i in range(self.length):
            self.minHeap[i] = (arr[i], i)
            self.maxHeap[i] = (arr[i], i)

        self.buildMaxHeap()
        self.buildMinHeap()

    def maxHeapify(self, i, n):
        l = left(i)
        r = right(i)

        max_ind = i
        if l < n and self.maxHeap[l][0] > self.maxHeap[max_ind][0]:
            max_ind = l
        if r < n and self.maxHeap[r][0] > self.maxHeap[max_ind][0]:
            max_ind = r

        if max_ind != i:
            swap(self.maxHeap, i, max_ind, self.minHeap)
            self.maxHeapify(max_ind, n)

    def buildMaxHeap(self):
        for i in range(parent(self.length - 1), -1, -1):
            self.maxHeapify(i, self.length)

    def minHeapify(self, i, n):
        l = left(i)
        r = right(i)

        min_idx = i
        if l < n and self.minHeap[l][0] < self.minHeap[min_idx][0]:
            min_idx = l
        if r < n and self.minHeap[r][0] < self.minHeap[min_idx][0]:
            min_idx = r

        if min_idx != i:
            swap(self.minHeap, i, min_idx, self.maxHeap)
            self.minHeapify(min_idx, n)

    def buildMinHeap(self):
        for i in range(parent(self.length - 1), -1, -1):
            self.minHeapify(i, self.length)

    def popMin(self):
        self.length -= 1
        swap(self.minHeap, 0, self.length, self.maxHeap)
        self.minHeapify(0, self.length)
        return self.minHeap[self.length]

    def popMax(self):
        self.length -= 1
        swap(self.maxHeap, 0, self.length, self.minHeap)
        self.maxHeapify(0, self.length)
        return self.maxHeap[self.length]

    def insert(self, value):
        if self.length == self.maxLength:
            print("Overflow.")
            return
        self.minHeap[self.length] = (value, self.length)
        self.maxHeap[self.length] = (value, self.length)
        self.length += 1

        i = self.length - 1
        p = parent(i)
        while p >= 0 and self.minHeap[i][0] < self.minHeap[p][0]:
            swap(self.minHeap, i, p, self.maxHeap)
            i = parent(i)
            p = parent(i)

        i = self.length - 1
        p = parent(i)
        while p >= 0 and self.maxHeap[i][0] > self.maxHeap[p][0]:
            swap(self.maxHeap, i, p, self.minHeap)
            i = parent(i)
            p = parent(i)

    def printMinHeap(self):
        print("MinHeap: [", end="")
        for i in range(self.length):
            print(self.minHeap[i], end="")
            if i != self.length - 1:
                print(", ", end="")
        print()

    def printMaxHeap(self):
        print("MaxHeap: [", end="")
        for i in range(self.length):
            print(self.maxHeap[i], end="")
            if i != self.length - 1:
                print(", ", end="")
        print()


if __name__ == '__main__':

    size = randint(10, 20)
    T = [randint(1, 20) for _ in range(size)]
    print("T =", T, end="\n\n")

    structure = TwinHeaps(T)

    structure.printMinHeap()
    structure.printMaxHeap()
    print()

    print("PopMax:", structure.popMax())
    structure.printMinHeap()
    structure.printMaxHeap()
    print()
    print("PopMin:", structure.popMin())
    structure.printMinHeap()
    structure.printMaxHeap()
    print()
    val = 15
    print("Insert:", val)
    structure.insert(val)
    structure.printMinHeap()
    structure.printMaxHeap()
    print()
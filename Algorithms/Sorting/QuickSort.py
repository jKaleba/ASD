import random


class Stack:
    stack = []
    size = 0
    def push(self, coords):
        self.stack.append(coords)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.stack.pop()

    def empty(self):
        return self.size == 0

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def partition(A, p, r):
    idx = random.randint(p, r)
    swap(A, idx, r)
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            swap(A, i, j)

    swap(A, i + 1, r)
    return i + 1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)

def quickSortI(A, p, r):
    st = Stack()
    st.push((p, r))

    while not st.empty():
        p, r = st.pop()
        if p < r:
            q = partition(A, p, r)
            st.push((p, q - 1))
            st.push((q + 1, r))


if __name__ == '__main__':
    S = [random.randint(0, 100) for _ in range(100)]
    n = len(S)
    quickSortI(S, 0, n - 1)
    print(S)
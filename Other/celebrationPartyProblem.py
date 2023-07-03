# The goal is to choose vertices with maximum fun,
# such that no two adjacent vertices are chosen

class Employee:
    def __init__(self, fun):
        self.employees = []
        self.fun = fun
        self.f = -1
        self.g = -1


#       f(v) - max fun for party in subtree rooted at v
#       g(v) - max fun for party in subtree rooted at v, if v is not invited

#       f(v) = max(fun(v) + g(u) for all u in v.employees, g(v))
#       g(v) = sum(f(u) for all u in v.employees )


def f(v: Employee):
    if v.f >= 0:
        return v.f

    x = v.fun
    for u in v.employees:
        x += g(u)

    y = g(v)
    v.f = max(x, y)

    return v.f


def g(v: Employee):
    if v.g >= 0:
        return v.g

    v.g = sum(f(u) for u in v.employees)
    return v.g


def maxFun(root: Employee):
    return max(f(root), g(root))


if __name__ == '__main__':
    root = Employee(4)

    B = Employee(7)
    C = Employee(2)
    D = Employee(5)

    E = Employee(3)
    F = Employee(1)
    G = Employee(6)

    H = Employee(2)
    I = Employee(4)
    J = Employee(3)

    root.employees = [B, C, D]
    B.employees = [E, F]
    D.employees = [G]
    E.employees = [H, I]
    G.employees = [J]

    max_fun = maxFun(root)
    print(max_fun)

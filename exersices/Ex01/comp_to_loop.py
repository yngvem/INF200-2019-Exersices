
n = 22


def squares_by_comp(n):
    loop = [k**2 for k in range(n) if k % 3 == 1]
    return loop


def squares_by_loop(n):
    loop = []
    for k in range(n):
        if k % 3 == 1:
            loop.append(k**2)
    return loop


a = squares_by_comp(n)
print(a)

b = squares_by_loop(n)
print(b)

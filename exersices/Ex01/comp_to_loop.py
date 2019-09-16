def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    lis = []
    for k in range(n):
        if k % 3 == 1:
            lis.append(k**2)
    return lis


a = squares_by_comp(10)

print(a)

b = squares_by_loop(10)

print(b)

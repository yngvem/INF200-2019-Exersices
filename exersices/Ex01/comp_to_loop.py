""" Task B: List comprehension to loot"""

n = 100


def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    k_list = []
    for k in range(n):
        if k % 3 == 1:
            k_list.append(k**2)
    return


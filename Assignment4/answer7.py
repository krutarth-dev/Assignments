def max_count(m, n, ops):
    if not ops:
        return m * n

    min_a = min(op[0] for op in ops)
    min_b = min(op[1] for op in ops)

    return min_a * min_b
m = 3
n = 3
ops = [[2, 2], [3, 3]]

max_integers = max_count(m, n, ops)
print(max_integers)

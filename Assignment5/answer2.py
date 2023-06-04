def complete_rows(n):
    k = 0
    while ((k * (k + 1)) // 2) <= n:
        k += 1
    return k - 1
n = 5
result = complete_rows(n)
print(result)


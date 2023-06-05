def generate_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    row_start, row_end = 0, n - 1
    col_start, col_end = 0, n - 1

    while row_start <= row_end and col_start <= col_end:
        for i in range(col_start, col_end + 1):
            matrix[row_start][i] = num
            num += 1
        row_start += 1

        for i in range(row_start, row_end + 1):
            matrix[i][col_end] = num
            num += 1
        col_end -= 1

        if row_start <= row_end:
            for i in range(col_end, col_start - 1, -1):
                matrix[row_end][i] = num
                num += 1
            row_end -= 1

        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                matrix[i][col_start] = num
                num += 1
            col_start += 1

    return matrix
n = 3
result = generate_spiral_matrix(n)
print(result)

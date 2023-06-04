def convert_to_2d_array(original, m, n):
    if m * n != len(original):
        return []  # Return an empty 2D array if it's impossible

    result = []
    index = 0
    for i in range(m):
        row = []
        for j in range(n):
            row.append(original[index])
            index += 1
        result.append(row)

    return result
original = [1, 2, 3, 4]
m = 2
n = 2
result = convert_to_2d_array(original, m, n)
print(result)

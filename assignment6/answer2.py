def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = left + (right - left) // 2
        mid_element = matrix[mid // cols][mid % cols]

        if mid_element == target:
            return True
        elif mid_element < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
result = search_matrix(matrix, target)
print(result)

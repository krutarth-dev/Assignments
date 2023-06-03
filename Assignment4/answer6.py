def sorted_squares(nums):
    n = len(nums)
    result = [0] * n  # Initialize a result array of the same size as nums
    left, right = 0, n - 1  # Pointers for the left and right ends of nums

    # Iterate from right to left in the result array
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1

    return result
nums = [-4, -1, 0, 3, 10]

squared_nums = sorted_squares(nums)
print(squared_nums)

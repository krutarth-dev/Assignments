def array_pair_sum(nums):
    nums.sort()  # Sort the array in ascending order
    max_sum = 0

    # Iterate through the array by skipping one element in each iteration
    for i in range(0, len(nums), 2):
        max_sum += nums[i]

    return max_sum
nums = [1, 4, 3, 2]

max_sum = array_pair_sum(nums)
print(max_sum)

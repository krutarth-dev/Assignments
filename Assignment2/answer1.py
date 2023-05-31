def arrayPairSum(nums):
    nums.sort()
    max_sum = 0
    for i in range(0, len(nums), 2):
        max_sum += min(nums[i], nums[i+1])
    return max_sum

nums = [1, 4, 3, 2]
print(arrayPairSum(nums))


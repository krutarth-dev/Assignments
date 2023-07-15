def find_missing_number(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    array_sum = sum(nums)
    return total_sum - array_sum
nums = [3, 0, 1]
print(find_missing_number(nums))  

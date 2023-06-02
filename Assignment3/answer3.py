def nextPermutation(nums):
    n = len(nums)
    i = n - 2

    # Find the first pair from the right where nums[i] < nums[i+1]
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        j = n - 1
        # Find the smallest element greater than nums[i] to its right
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # Reverse the subarray to the right of index i
    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# Example usage
nums = [1, 2, 3]
print("Original array:", nums)
nextPermutation(nums)
print("Next permutation:", nums)

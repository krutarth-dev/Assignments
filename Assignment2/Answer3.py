def findLHS(nums):
    count = {}
    max_length = 0

    # Count the occurrences of each number
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # Check for harmonious subsequences
    for num in count:
        if num + 1 in count:
            length = count[num] + count[num + 1]
            max_length = max(max_length, length)

    return max_length
nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(findLHS(nums))

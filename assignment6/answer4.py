def find_max_length(nums):
    counts = {0: -1}
    count = 0
    max_length = 0

    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1

        if count in counts:
            length = i - counts[count]
            max_length = max(max_length, length)
        else:
            counts[count] = i

    return max_length
nums = [0, 1]
result = find_max_length(nums)
print(result)

def findMissingRanges(nums, lower, upper):
    result = []
    start = lower

    for num in range(lower, upper + 1):
        if num in nums:
            if start != num:
                if start == num - 1:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(num - 1))
            start = num + 1

    if start <= upper:
        if start == upper:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(upper))

    return result


# Example usage
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99

result = findMissingRanges(nums, lower, upper)
print("Missing ranges:", result)


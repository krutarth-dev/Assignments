def intersection(nums1, nums2):
    set_nums1 = set(nums1)
    result = set()

    for num in nums2:
        if num in set_nums1:
            result.add(num)

    return list(result)
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))  

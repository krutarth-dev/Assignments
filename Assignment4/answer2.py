def find_disjoint_elements(nums1, nums2):
    set1 = set(nums1)  # Convert nums1 to a set
    set2 = set(nums2)  # Convert nums2 to a set

    # Find the distinct elements in nums1 but not in nums2
    distinct_nums1 = list(set1 - set2)

    # Find the distinct elements in nums2 but not in nums1
    distinct_nums2 = list(set2 - set1)

    return [distinct_nums1, distinct_nums2]
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

answer = find_disjoint_elements(nums1, nums2)
print(answer)

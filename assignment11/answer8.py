from collections import Counter

def intersect(nums1, nums2):
    counter1 = Counter(nums1)
    counter2 = Counter(nums2)
    intersection = []

    for num, freq in counter1.items():
        if num in counter2:
            intersection.extend([num] * min(freq, counter2[num]))

    return intersection
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2)) 

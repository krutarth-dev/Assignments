def findMax(arr, n):
    # Base case: If there is only one element in the array, return it
    if n == 1:
        return arr[0]

    # Recursive case: Find the maximum element in the subarray excluding the last element
    max_num = findMax(arr, n - 1)

    # Compare the maximum element with the last element of the array
    if arr[n - 1] > max_num:
        return arr[n - 1]
    else:
        return max_num
arr = [1, 4, 3, -5, -4, 8, 6]
n = len(arr)
print(findMax(arr, n))  

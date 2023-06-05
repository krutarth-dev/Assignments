def valid_mountain_array(arr):
    n = len(arr)
    if n < 3:
        return False

    i = 0
    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1

    if i == 0 or i == n - 1:
        return False

    while i < n - 1 and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1
arr = [2, 1]
result = valid_mountain_array(arr)
print(result)

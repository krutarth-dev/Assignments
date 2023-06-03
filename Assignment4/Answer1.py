def find_common_elements(arr1, arr2, arr3):
    i = j = k = 0  # Pointers for each array
    result = []  # Store the common elements
    
    # Iterate until one of the arrays reaches its end
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            # Found a common element
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    
    return result
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]

common_elements = find_common_elements(arr1, arr2, arr3)
print(common_elements)

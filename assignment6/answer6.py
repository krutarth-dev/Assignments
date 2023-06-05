def find_original_array(changed):
    count = {}
    for num in changed:
        count[num] = count.get(num, 0) + 1

    original = []
    for num in changed:
        if count.get(num, 0) > 0:
            original.append(num)
            count[num] -= 1
            count[num*2] -= 1
        elif count.get(num*2, 0) > 0:
            return []  # Invalid doubled array

    return original
changed = [1, 3, 4, 2, 6, 8]
original = find_original_array(changed)
print(original)

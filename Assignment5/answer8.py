def find_original(changed):
    original_set = set()

    for num in changed:
        if num % 2 == 0 and num // 2 in original_set:
            original_set.remove(num // 2)
        else:
            original_set.add(num)

    if len(original_set) == 0:
        return list(original_set)
    else:
        return []
changed = [1, 3, 4, 2, 6, 8]
result = find_original(changed)
print(result)

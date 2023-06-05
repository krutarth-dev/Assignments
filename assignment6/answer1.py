def reconstruct_permutation(s):
    n = len(s)
    perm = [0] * (n + 1)
    
    current_min = 0
    current_max = n
    
    for i in range(n):
        if s[i] == 'I':
            perm[i] = current_min
            current_min += 1
        else:
            perm[i] = current_max
            current_max -= 1

    perm[n] = current_min

    return perm
s = "IDID"
result = reconstruct_permutation(s)
print(result)

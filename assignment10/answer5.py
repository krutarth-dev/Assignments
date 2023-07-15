def count_contiguous_substrings(S):
    count = 0
    for i in range(len(S)):
        count += 1
        j = i + 1
        while j < len(S) and S[j] == S[i]:
            count += 1
            j += 1
    return count
print(count_contiguous_substrings("abcab"))  

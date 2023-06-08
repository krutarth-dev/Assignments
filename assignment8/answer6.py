from collections import Counter

def findAnagrams(s, p):
    p_freq = Counter(p)
    s_freq = Counter(s[:len(p)])
    result = []

    if p_freq == s_freq:
        result.append(0)

    for i in range(len(p), len(s)):
        s_freq[s[i-len(p)]] -= 1
        if s_freq[s[i-len(p)]] == 0:
            del s_freq[s[i-len(p)]]
        s_freq[s[i]] += 1

        if p_freq == s_freq:
            result.append(i - len(p) + 1)

    return result

# Testing the example
s = "cbaebabacd"
p = "abc"
indices = findAnagrams(s, p)
print(indices)  # Output: [0, 6]

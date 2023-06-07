def reverseStr(s, k):
    result = ""

    for i in range(0, len(s), 2*k):
        # Reverse the first k characters
        result += s[i:i+k][::-1]
        # Append the remaining characters as they are
        result += s[i+k:i+2*k]

    return result

# Example usage
s = "abcdefg"
k = 2
print(reverseStr(s, k))  # Output: "bacdfeg"

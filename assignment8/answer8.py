def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False

    if s == goal:
        # Check if s has at least one repeated character
        return len(set(s)) < len(s)

    diff_indices = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diff_indices.append(i)

    return len(diff_indices) == 2 and s[diff_indices[0]] == goal[diff_indices[1]] and s[diff_indices[1]] == goal[diff_indices[0]]

# Testing the example
s = "ab"
goal = "ba"
result = buddyStrings(s, goal)
print(result)  # Output: True

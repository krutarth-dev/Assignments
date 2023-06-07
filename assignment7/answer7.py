def processString(s):
    stack = []
    for char in s:
        if char != '#':
            stack.append(char)
        elif stack:
            stack.pop()
    return ''.join(stack)


def backspaceCompare(s, t):
    processed_s = processString(s)
    processed_t = processString(t)
    return processed_s == processed_t

# Example usage
s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t))  # Output: True

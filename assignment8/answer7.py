def decodeString(s):
    stack = []
    current_string = ""
    current_count = 0

    for char in s:
        if char.isdigit():
            current_count = current_count * 10 + int(char)
        elif char == "[":
            stack.append(current_string)
            stack.append(current_count)
            current_string = ""
            current_count = 0
        elif char == "]":
            count = stack.pop()
            prev_string = stack.pop()
            current_string = prev_string + count * current_string
        else:
            current_string += char

    return current_string

# Testing the example
s = "3[a]2[bc]"
decoded_string = decodeString(s)
print(decoded_string)  # Output: "aaabcbc"

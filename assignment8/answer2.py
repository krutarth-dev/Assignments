def checkValidString(s):
    stack = []
    asterisks = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == '*':
            asterisks.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            elif asterisks:
                asterisks.pop()
            else:
                return False
    
    while stack and asterisks:
        if stack[-1] < asterisks[-1]:
            stack.pop()
            asterisks.pop()
        else:
            break
    
    return len(stack) == 0

# Testing the example
s = "()"
print(checkValidString(s))  # Output: True

def addStrings(num1, num2):
    result = ""
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0

    while i >= 0 or j >= 0:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0

        sum_digits = digit1 + digit2 + carry
        carry = sum_digits // 10
        current_digit = sum_digits % 10

        result = str(current_digit) + result

        i -= 1
        j -= 1

    if carry > 0:
        result = str(carry) + result

    return result

# Example usage
num1 = "11"
num2 = "123"
print(addStrings(num1, num2))  # Output: "134"

def compress(chars):
    write = anchor = 0
    count = 1
    
    for read in range(1, len(chars)):
        if chars[read] == chars[read - 1]:
            count += 1
        else:
            chars[write] = chars[anchor]
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            anchor = read
            count = 1
    
    chars[write] = chars[anchor]
    write += 1
    if count > 1:
        for digit in str(count):
            chars[write] = digit
            write += 1
    
    return write

# Testing the example
chars = ["a", "a", "b", "b", "c", "c", "c"]
length = compress(chars)
print(length)  # Output: 6
print(chars[:length])  # Output: ["a", "2", "b", "2", "c", "3"]

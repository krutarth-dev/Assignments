def last_remaining(n):
    left_to_right = True
    remaining = n
    step = 1
    start = 1

    while remaining > 1:
        if left_to_right or remaining % 2 == 1:
            start += step

        remaining //= 2
        step *= 2
        left_to_right = not left_to_right

    return start

print(last_remaining(9)) 

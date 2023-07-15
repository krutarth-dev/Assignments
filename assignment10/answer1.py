import math

def is_power_of_three(n):
    if n <= 0:
        return False
    x = math.log(n, 3)
    return x == int(x)
print(is_power_of_three(-1))  # Output: False

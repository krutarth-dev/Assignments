def canShift(s, goal):
    if len(s) != len(goal):
        return False

    double_s = s + s
    if goal in double_s:
        return True
    else:
        return False

# Example usage
s = "abcde"
goal = "cdeab"
print(canShift(s, goal))  # Output: True

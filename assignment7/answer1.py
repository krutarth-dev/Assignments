def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False

    s_map = {}
    t_map = {}

    for s_char, t_char in zip(s, t):
        if s_char in s_map:
            if s_map[s_char] != t_char:
                return False
        if t_char in t_map:
            if t_map[t_char] != s_char:
                return False
        s_map[s_char] = t_char
        t_map[t_char] = s_char

    return True

# Example usage
s = "egg"
t = "add"
print(isomorphic_strings(s, t))  # Output: True

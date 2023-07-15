def calculate_length(string):
    if string == "":
        return 0
    elif len(string) == 1:
        return 1
    else:
        return 1 + calculate_length(string[1:])

print(calculate_length("abcd")) 

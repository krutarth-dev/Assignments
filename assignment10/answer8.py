def count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0

    for char in string:
        if char in consonants:
            count += 1

    return count
print(count_consonants("abc de")) 

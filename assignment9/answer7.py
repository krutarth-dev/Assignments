def generatePermutations(s, l, r):
    if l == r:
        print(''.join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]  # Swap characters
            generatePermutations(s, l + 1, r)  # Recursively generate permutations for the remaining characters
            s[l], s[i] = s[i], s[l]  # Backtrack 

def printPermutations(S):
    s = list(S)  # Convert string to a list of characters
    n = len(s)
    generatePermutations(s, 0, n - 1)
    
S = "ABC"
printPermutations(S)



def maxCandies(candyType):
    max_eaten = len(set(candyType))
    max_allowed = len(candyType) 
    return min(max_eaten, max_allowed)
    
candyType = [1, 1, 2, 2,4,4]
print(maxCandies(candyType))

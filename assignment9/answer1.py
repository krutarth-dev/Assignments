def isPowerOfTwo(n):
    if n <= 0:
        return False

    while n > 1:
        if n & 1 != 0:
            return False
        n >>= 1

    return True
print(isPowerOfTwo(1)) 
print(isPowerOfTwo(16))  
print(isPowerOfTwo(3))  

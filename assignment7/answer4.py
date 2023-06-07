def reverseWords(s):
    words = s.split()  # Split the string into individual words
    reversed_words = [word[::-1] for word in words]  # Reverse the characters in each word
    reversed_sentence = ' '.join(reversed_words)  # Join the reversed words with whitespace
    return reversed_sentence

# Example usage
s = "Let's take LeetCode contest"
print(reverseWords(s))  # Output: "s'teL ekat edoCteeL tsetnoc"

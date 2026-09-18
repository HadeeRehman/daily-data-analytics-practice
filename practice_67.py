# Find the first unique character in a string using a frequency dictionary

def unique(s):
    count = {}

    for char in s:
        lower_char = char.lower()
        count[lower_char] = count.get(lower_char, 0) + 1

    for char in s:
        if char.isalpha() and count[char.lower()] == 1:
            return char
    return None


print(unique("aabbccd"))  # Output: d
print(unique("Google"))   # Output: l
# Count vowels and consonants in a string using dictionary accumulators

def count_vowels_consonants(s):
    count = {"vowels" : 0, "consonants" : 0}
    for char in s:
        if char.isalpha():
            if char.lower() in "aeiou":
                count["vowels"] += 1
            else:
                count["consonants"] += 1
    return count
print(count_vowels_consonants("Python 3.9"))
print(count_vowels_consonants("Hello World"))
print(count_vowels_consonants("AEIOU aeiou"))
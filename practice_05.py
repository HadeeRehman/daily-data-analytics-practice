# Question: Find words with more than 5 letters and save their lengths.

words = ["apple", "banana", "orange", "kiwi", "mango"]
report = {}

for word in words:
    if len(word) > 5:
        report[word] = len(word)

print(report)

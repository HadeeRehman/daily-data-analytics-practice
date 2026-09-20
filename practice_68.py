# Find the most frequent character and its frequency count in a string

text = 'Programming'

def highest_char(text):
    if not text :
        return None
    
    count = {}

    for char in text:
        count[char] = count.get(char, 0) + 1
    

    highest = 0
    most_repeated = ''


    for char, val in count.items():
        if val > highest:
            highest = val
            most_repeated = char
    return highest, most_repeated
print(highest_char(text))
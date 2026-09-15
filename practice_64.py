# Build friend-language dictionary with interactive duplicate key validation

d = {}


for i in range(3):
    name = input("Enter friend's name: ")

    # Check for duplicates
    while name in d:
        print("This name is already taken. Try a different name.")
        name = input("Enter a different friend's name: ")

    lang = input("Enter friend's language: ")
    d[name] = lang # or d.update({name:lang})

print("\nFinal Dictionary of Friends & Languages:")
print(d)

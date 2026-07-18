# Quick exercise testing how to modify a mutable list wrapped inside an immutable tuple.
# Goal: Add 'python' to Mujtaba's skills list without breaking the tuple structure.

employes = [
    (101, 'Hadi',["python",'c++']),
    (102, 'Mujtaba',['power Bi'])
]
employes[1][2].append('python')
print(employes)

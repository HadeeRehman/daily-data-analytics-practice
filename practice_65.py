# Collect even numbers up to n into a tuple using loop concatenation
def count_even(n):
    count = ()

    for i in range(2, n + 1):
        if i % 2 == 0:
            count +=(i,)
    return count
print(count_even(10))

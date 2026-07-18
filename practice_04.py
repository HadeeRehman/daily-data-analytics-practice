# Question: Count the frequency of each fruit in the list using a dictionary.
# This mimics a basic SQL "GROUP BY COUNT" aggregation using pure Python logic.

purchased_items = ["apple", "banana", "apple", "orange", "banana", "apple"]
report = {}

for fruit in purchased_items:
    if fruit in report:
        report[fruit] = report[fruit] + 1  # Increment count if already tracked
    else:
        report[fruit] = 1                  # Initialize count if seen for the first time

print(report)

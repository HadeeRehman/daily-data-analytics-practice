# Question: Clean a list of scores by removing None values and out-of-range scores (must be between 0 and 100).

# --- Method 1: Standard Loop with Direct Key Lookup ---

# --- Method 2: Standard Loop with a Temporary Variable ---

# --- Method 3: Clean One-Line List Comprehension ---

scores = [
    {"name": "Alice", "score": 85},
    {"name": "Bob",   "score": None},
    {"name": "Charlie", "score": 92},
    {"name": "Dave",  "score": -5},
    {"name": "Eve",   "score": 78},
    {"name": "Frank", "score": 150},
    {"name": "Grace", "score": 60},
]
def clean_scores(scores):
    result = []
    for score in scores:
        if score['score'] != None and 0 <= score['score'] <= 100:
            result.append(score)
    return result
    # for sale in scores:
    #     score = sale['score']
    #     if score != None and 0 <= score <= 100:
    #         new.append(sale)

    # return new
    #     return [score for score in scores if score['score'] != None and  0 <= score['score'] <= 100]
print(clean_scores(scores))

# Filter students scoring 70 or above, group them by subject, and sort them by score in descending order.
students = [
    {"name": "Alice",   "subject": "Math",    "score": 88, "grade": "A"},
    {"name": "Bob",     "subject": "Science",  "score": 55, "grade": "C"},
    {"name": "Charlie", "subject": "Math",    "score": 72, "grade": "B"},
    {"name": "Diana",   "subject": "Science",  "score": 91, "grade": "A"},
    {"name": "Eve",     "subject": "Math",    "score": 40, "grade": "F"},
    {"name": "Frank",   "subject": "Science",  "score": 78, "grade": "B"},
    {"name": "Grace",   "subject": "Math",    "score": 95, "grade": "A"},
    {"name": "Hank",    "subject": "Science",  "score": 43, "grade": "F"},
]
def subject_toppers(students):
    data = {}
    score_lookup = {}
    for student in students:
        score_lookup[student['name']] = student['score']
        if student['subject'] not in data:
            data[student['subject']] = []
        if student['score'] >= 70:
            data[student['subject']].append(student['name'])
    # result = {}
    # for subject in data:
    #     result[subject] = sorted(data[subject], key= lambda name: score_lookup[name], reverse=True) # key=lambda name: score_loopup[name] ->
    # means take name from data[subject] for eg subject is math inside it is alice, charlie etc so it takes name from it its like what in inside math like lambda x
    # return result
    return {subject: sorted(data[subject], key=lambda name: score_lookup[name], reverse=True) for subject in data} # key=lambda x -> inside new becomes x
print(subject_toppers(students))
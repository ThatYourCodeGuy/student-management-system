def get_highest_score(students):
    # This will fail if students list is empty
    return max(student["score"] for student in students)

def get_lowest_score(students):
    # This will fail if students list is empty
    return min(student["score"] for student in students)
from typing import List, Optional
from students import Student
import statistics

def get_highest_score(students: List[Student]) -> Optional[float]:
    if not students: return None
    return max(student.score for student in students)

def get_lowest_score(students: List[Student]) -> Optional[float]:
    if not students: return None
    return min(student.score for student in students)

def get_median_score(students: List[Student]) -> Optional[float]:
    if not students: return None
    scores = [student.score for student in students]
    return statistics.median(scores)
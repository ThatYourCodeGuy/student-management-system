import statistics
from typing import List, Optional
from models.student import Student

def get_highest_score(students: List[Student]) -> Optional[float]:
    """Calculates the highest score safely."""
    if not students:
        return None
    return max(student.score for student in students)

def get_lowest_score(students: List[Student]) -> Optional[float]:
    """Calculates the lowest score safely."""
    if not students:
        return None
    return min(student.score for student in students)

def get_median_score(students: List[Student]) -> Optional[float]:
    """Calculates the median score."""
    if not students:
        return None
    scores = [student.score for student in students]
    return statistics.median(scores)
from pydantic import BaseModel, Field
from typing import List

class Student(BaseModel):
    name: str
    score: float = Field(ge=0, le=100)

# Raw data (could be empty)
raw_students_data = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
    # {"name": "Invalid", "score": 150}, # Example of invalid data
]

# Validate data and store as a list of Student objects
students: List[Student] = []
for data in raw_students_data:
    try:
        students.append(Student(**data))
    except Exception as e:
        print(f"Skipping invalid student record: {data} - {e}")
from pydantic import BaseModel, Field
from typing import List

class Student(BaseModel):
    name: str
    score: float = Field(ge=0, le=100)

raw_students_data = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
]

students: List[Student] = []
for data in raw_students_data:
    try:
        students.append(Student(**data))
    except Exception as e:
        print(f"Skipping invalid student record: {data} - {e}")
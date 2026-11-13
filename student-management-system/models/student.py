from pydantic import BaseModel, Field

class Student(BaseModel):
    """Data model for a Student."""
    name: str
    score: float = Field(ge=0, le=100)
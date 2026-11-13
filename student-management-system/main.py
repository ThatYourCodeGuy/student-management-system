from database import get_db_connection
from models.student import Student
from controllers.stats_controller import get_highest_score, get_lowest_score, get_median_score

def fetch_students() -> list[Student]:
    """Fetches all students from the SQLite database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, score FROM students")
    rows = cursor.fetchall()
    conn.close()
    
    return [Student(name=row["name"], score=row["score"]) for row in rows]

def main():
    print("===============================")
    print("   STUDENT MANAGEMENT SYSTEM   ")
    print("   (SQLite Backend)            ")
    print("===============================")
    
    students = fetch_students()

    if not students:
        print("No student data available in the database.")
        return

    highest = get_highest_score(students)
    lowest = get_lowest_score(students)
    median = get_median_score(students)

    print(f"Total Students : {len(students)}")
    print(f"Highest Score  : {highest}")
    print(f"Lowest Score   : {lowest}")
    print(f"Median Score   : {median}")
    print("===============================")

if __name__ == "__main__":
    main()
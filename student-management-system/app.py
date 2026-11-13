from students import students
from utils.helpers import get_highest_score, get_lowest_score

if __name__ == "__main__":
    print("Student Management System")
    print("-------------------------")
    print(f"Highest Score: {get_highest_score(students)}")
    print(f"Lowest Score: {get_lowest_score(students)}")
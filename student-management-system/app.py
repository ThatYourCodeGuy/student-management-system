from students import students
from utils.helpers import get_highest_score, get_lowest_score, get_median_score

def main():
    print("===============================")
    print("   STUDENT MANAGEMENT SYSTEM   ")
    print("===============================")
    
    if not students:
        print("No student data available.")
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
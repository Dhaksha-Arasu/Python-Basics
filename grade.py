n = int(input())
grades = []
for i in range(1,n+1):
    while True:
        try:
            grade = float(input(f"Subject {i}: "))
            if 0<= grade <= 100:
                grades.append(grade)
                break
            else:
                print("Invalid Marks")
        except ValueError:
                print("Invalid input")
average = sum(grades) / n
grade_letter = (
    'A' if average >= 90 else
    'B' if average >= 80 else
    'C' if average >= 70 else
    'D' if average >= 60 else
    'F'
)
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade_letter}")
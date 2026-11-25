def calculate_total(marks):
    total = sum(marks)
    return total

def calculate_percentage(total):
    percentage = total / 5
    return percentage

def calculate_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"

def generate_result():
    name = input("Enter student name: ")

    subjects = ["English", "Maths", "Science", "Computer", "History"]
    marks = []

    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        marks.append(mark)

    total = calculate_total(marks)
    percentage = calculate_percentage(total)
    grade = calculate_grade(percentage)

    report = f"""
    ========== STUDENT RESULT ==========
    Student Name: {name}
    Subject          Marks
    ------------------------------------"""

    for subject, mark in zip(subjects, marks):
        report += f"{subject:<17} {mark:.2f}\n"

    report += f"""------------------------------------
    Total Marks: {total:.2f} / 500
    Percentage: {percentage:.2f}%
    Grade: {grade}
    ===================================="""

    print(report)

    with open("result.txt", "w") as file:
        file.write(report)

    print("Result saved successfully in result.txt!")

def main():
    generate_result()

main()
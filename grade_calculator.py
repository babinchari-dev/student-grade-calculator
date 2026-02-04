def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        return "A+"
    elif average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "Fail"


if __name__ == "__main__":
    marks = []

    for i in range(5):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    grade = calculate_grade(marks)
    print("Grade:", grade)
